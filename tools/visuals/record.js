// Records a short loop of a page for the website: a visible pointer, real clicks, frames taken as sharp
// screenshots of one region, then encoded as WebM and MP4 with a still for visitors who switched motion off.
//   const rec = new Recorder(page, { x, y, width, height });
//   await rec.hold(800); await rec.click(x, y); await rec.hold(1500); await rec.save('img/loops/name-en');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const POINTER = `
(() => {
  const p = document.createElement('div'); p.id = 'site-pointer';
  p.style.cssText = 'position:fixed;left:0;top:0;width:22px;height:22px;margin:-11px 0 0 -11px;border-radius:50%;' +
    'background:rgba(255,255,255,.6);box-shadow:0 0 0 2px rgba(255,255,255,.95),0 0 0 4px rgba(17,19,24,.7),0 4px 14px rgba(0,0,0,.6);' +
    'pointer-events:none;z-index:2147483647;transform:translate(-100px,-100px)';
  const r = document.createElement('div'); r.id = 'site-ripple';
  r.style.cssText = 'position:absolute;inset:-2px;border-radius:50%;border:3px solid #fff;opacity:0;';
  p.appendChild(r); document.body.appendChild(p);
  window.__pointer = (x, y, ripple) => {
    p.style.transform = 'translate(' + x + 'px,' + y + 'px) scale(' + (ripple > 0 && ripple < 0.35 ? 0.82 : 1) + ')';
    r.style.opacity = ripple > 0 ? String(1 - ripple) : '0';
    r.style.transform = 'scale(' + (1 + ripple * 1.6) + ')';
  };
})();`;

class Recorder {
  constructor(page, clip) {
    this.page = page; this.clip = clip; this.frames = [];
    this.dir = fs.mkdtempSync(path.join(os.tmpdir(), 'loop-'));
    this.at = { x: clip.x + clip.width * 0.82, y: clip.y + clip.height * 0.86 };
  }
  async start() { await this.page.evaluate(POINTER); await this.page.mouse.move(this.at.x, this.at.y); }
  async frame(ms, ripple = 0) {
    await this.page.evaluate(([x, y, r]) => window.__pointer(x, y, r), [this.at.x, this.at.y, ripple]);
    const file = path.join(this.dir, String(this.frames.length).padStart(5, '0') + '.png');
    await this.page.screenshot({ path: file, clip: this.clip });
    this.frames.push({ file, ms });
  }
  /** Stay for a while; a frame every 100 ms keeps live meters moving. */
  async hold(ms) {
    for (let t = 0; t < ms; t += 100) { await this.frame(Math.min(100, ms - t)); await this.page.waitForTimeout(40); }
  }
  async moveTo(x, y, ms = 650) {
    const from = { ...this.at }, steps = Math.max(2, Math.round(ms / 40));
    for (let i = 1; i <= steps; i++) {
      const k = i / steps, e = k < 0.5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;  // ease in and out
      this.at = { x: from.x + (x - from.x) * e, y: from.y + (y - from.y) * e };
      await this.page.mouse.move(this.at.x, this.at.y);
      await this.frame(40);
    }
  }
  async click(x, y) {
    await this.moveTo(x, y);
    await this.hold(180);
    await this.frame(60, 0.15);
    await this.page.mouse.click(x, y);
    for (const r of [0.35, 0.6, 0.85]) await this.frame(70, r);
    // Step aside, so the pointer does not cover what the click changed.
    await this.moveTo(x + 34, y + 20, 240);
  }
  /** Writes <base>.webm, <base>.mp4 and <base>.webp (the last frame before the loop closes). */
  async save(base, width = 1280) {
    const last = this.frames[this.frames.length - 1].file, first = this.frames[0].file;
    // Close the loop: eight blended frames from the end back to the start.
    const blends = [];
    for (let i = 1; i <= 8; i++) {
      const out = path.join(this.dir, `blend-${i}.png`);
      execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', last, '-i', first, '-filter_complex', `[0][1]blend=all_expr='A*(1-${i / 9})+B*${i / 9}'`, out]);
      blends.push({ file: out, ms: 45 });
    }
    const list = path.join(this.dir, 'list.txt');
    const all = [...this.frames, ...blends];
    fs.writeFileSync(list, 'ffconcat version 1.0\n' + all.map((f) => `file '${f.file}'\nduration ${(f.ms / 1000).toFixed(3)}`).join('\n') + `\nfile '${all[all.length - 1].file}'\n`);
    fs.mkdirSync(path.dirname(base), { recursive: true });
    const vf = `fps=25,scale=${width}:-2:flags=lanczos`;
    const input = ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list];
    execFileSync('ffmpeg', [...input, '-vf', vf, '-an', '-c:v', 'libvpx-vp9', '-crf', '36', '-b:v', '0', '-row-mt', '1', '-pix_fmt', 'yuv420p', base + '.webm']);
    execFileSync('ffmpeg', [...input, '-vf', vf, '-an', '-c:v', 'libx264', '-crf', '27', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', base + '.mp4']);
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', last, '-vf', `scale=${width}:-2:flags=lanczos`, '-quality', '84', base + '.webp']);
    const total = all.reduce((s, f) => s + f.ms, 0);
    fs.rmSync(this.dir, { recursive: true, force: true });
    return { seconds: total / 1000, webm: fs.statSync(base + '.webm').size, mp4: fs.statSync(base + '.mp4').size };
  }
}
module.exports = { Recorder };

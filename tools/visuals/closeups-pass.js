// The website's close-ups of Spectacast Pass, taken from the Demo Congress 2027 in every language.
//   node tools/visuals/closeups-pass.js <pass repo, npm installed> [en,de,es,it]
// pass-answers: the door app's three answers side by side. Each is the real page on a phone-sized screen
// (green: a first entry; amber: the same badge at an entry-only door while it is inside; red: a code nobody has);
// only the frames around them are drawn.
const { chromium } = require('playwright');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const { withPass } = require('./pass-demo');

const [repo, langs = 'en,de,es,it'] = process.argv.slice(2);
if (!repo) throw new Error('usage: closeups-pass.js <pass repo> [languages]');
const OUT = process.env.OUT || path.join(__dirname, '..', '..', 'img', 'closeups');
fs.mkdirSync(OUT, { recursive: true });
const LOCALE = { en: 'en-GB', de: 'de-DE', es: 'es-ES', it: 'it-IT' };
const W = 390, H = 700;            // the phone's screen
const SHOWN = 236, GAP = 34, PAD = 26, EDGE = 9;   // on the picture: a screen's width, the space between, around, the frame

(async () => {
  const browser = await chromium.launch();
  for (const lang of langs.split(',')) {
    await withPass(repo, lang, async ({ base, info }) => {
      const when = Date.parse(info.snapshotAt);
      const door = (mode) => `${base}/scan?event=${info.event}&door=${info.door}&name=${encodeURIComponent(info.doorName)}${mode ? '&mode=' + mode : ''}`;
      // What is scanned, where and when: the second scan is twelve minutes later, at the door set to entry only.
      const scans = [[door(''), info.guest, 0], [door('in'), info.guest, 12 * 60_000], [door(''), 'NOBODY2027', 13 * 60_000]];
      const shots = [];
      for (const [url, code, later] of scans) {
        const ctx = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, colorScheme: 'light', timezoneId: 'Europe/Berlin', locale: LOCALE[lang] });
        const page = await ctx.newPage();
        await page.clock.setFixedTime(new Date(when + later));
        await page.goto(url); await page.waitForTimeout(1500);
        await page.keyboard.type(code, { delay: 5 }); await page.keyboard.press('Enter'); await page.waitForTimeout(800);
        shots.push((await page.screenshot()).toString('base64'));
        await ctx.close();
      }
      const shownH = Math.round(SHOWN * H / W), width = PAD * 2 + SHOWN * 3 + EDGE * 6 + GAP * 2, height = PAD * 2 + shownH + EDGE * 2;
      const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 2 });
      await page.setContent(`<style>
        body { margin: 0; background: #f3f1ea; display: flex; gap: ${GAP}px; padding: ${PAD}px; }
        div { padding: ${EDGE}px; border-radius: 30px; background: #111318; box-shadow: 0 14px 30px rgba(17,19,24,.25); }
        img { display: block; width: ${SHOWN}px; height: ${shownH}px; border-radius: 22px; }
      </style>${shots.map((s) => `<div><img src="data:image/png;base64,${s}"></div>`).join('')}`);
      const png = path.join(OUT, `pass-answers-${lang}.png`);
      await page.screenshot({ path: png });
      await page.close();
      execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', png, '-quality', '88', png.replace('.png', '.webp')]);
      fs.rmSync(png);
      // One mark on the top edge of each phone.
      const marks = [0, 1, 2].map((i) => [+(((PAD + EDGE + SHOWN / 2 + i * (SHOWN + EDGE * 2 + GAP)) / width) * 100).toFixed(1), +((PAD / height) * 100).toFixed(1)]);
      fs.writeFileSync(path.join(OUT, `pass-answers-${lang}.json`), JSON.stringify({ marks }) + '\n');
      console.log(`img/closeups/pass-answers-${lang}.webp`);
    });
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });

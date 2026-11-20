// The website's loops of Spectacast Director, recorded from the Demo Congress 2027 in every language.
//   node tools/visuals/loops-director.js <director repo, npm installed> [en,de,es,it] [loop names]
const { chromium } = require('playwright');
const path = require('node:path');
const { withDirector } = require('./director-demo');
const { Recorder } = require('./record');

const [repo, langs = 'en,de,es,it', only = ''] = process.argv.slice(2);
if (!repo) throw new Error('usage: loops-director.js <director repo> [languages] [loops]');
const OUT = path.join(__dirname, '..', '..', 'img', 'loops');

/** The buttons of the bar above the halls, left to right, once someone is picked. */
const bar = (page) => page.evaluate(() => [...document.querySelectorAll('button')]
  .map((b) => b.getBoundingClientRect()).filter((r) => r.top > 150 && r.bottom < 200 && r.width > 40)
  .sort((a, b) => a.left - b.left).map((r) => ({ x: r.left + r.width / 2, y: r.top + r.height / 2 })));

const LOOPS = {
  // Pick a speaker, open their microphone, put them in the spotlight.
  'director-speaker': async (page) => {
    const rec = new Recorder(page, { x: 22, y: 142, width: 664, height: 280 });
    await rec.start(); await rec.hold(900);
    const row = await page.getByText('Dr. Elena Ortega').first().boundingBox();
    await rec.click(row.x + row.width / 2, row.y + row.height / 2); await rec.hold(700);
    const b = await bar(page);
    await rec.click(b[3].x, b[3].y); await rec.hold(1500);   // Muted becomes Mic on
    await rec.click(b[1].x, b[1].y); await rec.hold(2200);   // Spotlight
    return rec;
  },
  // Put a clip on air: the hall's own microphone mutes by itself.
  'director-clip': async (page) => {
    const rec = new Recorder(page, { x: 244, y: 196, width: 440, height: 652 });
    await rec.start(); await rec.hold(1000);
    await rec.click(404, 751); await rec.hold(3000);          // Program: VOD
    await rec.click(404, 677); await rec.hold(1800);          // Program: back to the meeting
    return rec;
  },
};

(async () => {
  const browser = await chromium.launch();
  for (const lang of langs.split(',')) {
    for (const name of Object.keys(LOOPS).filter((n) => !only || only.split(',').includes(n))) {
      await withDirector(repo, lang, async (url) => {
        const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, locale: lang, deviceScaleFactor: 2 });
        await page.goto(url); await page.waitForTimeout(3000);
        const rec = await LOOPS[name](page);
        const info = await rec.save(path.join(OUT, `${name}-${lang}`), Math.min(1280, rec.clip.width * 2));
        console.log(`${name}-${lang}: ${info.seconds.toFixed(1)} s, webm ${Math.round(info.webm / 1024)} KB, mp4 ${Math.round(info.mp4 / 1024)} KB`);
        await page.close();
      });
    }
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });

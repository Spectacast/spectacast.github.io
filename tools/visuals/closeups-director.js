// The website's close-ups of Spectacast Director: one region of a page, sharp, in every language.
//   node tools/visuals/closeups-director.js <director repo, npm installed> [en,de,es,it]
const { chromium } = require('playwright');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const { withDirector } = require('./director-demo');

const [repo, langs = 'en,de,es,it'] = process.argv.slice(2);
if (!repo) throw new Error('usage: closeups-director.js <director repo> [languages]');
const OUT = path.join(__dirname, '..', '..', 'img', 'closeups');
fs.mkdirSync(OUT, { recursive: true });

// tab: the place of the page's tab in the header (0 is Panels); clip: the region, in page pixels at 1600 wide;
// marks: where the numbered marks go, in page pixels. The hall's are fixed (its strip is laid out the same in every
// language); the fleet's are read from the page, because its columns move with the words.
const CLOSEUPS = [
  { name: 'director-hall', tab: 0, clip: { x: 240, y: 192, width: 452, height: 312 },
    marks: async () => [[446, 220], [446, 258], [446, 429]] },
  // Beside the titles of the helper, users and waiting columns.
  { name: 'director-fleet', tab: 2, clip: { x: 160, y: 120, width: 760, height: 198 },
    marks: (page) => page.evaluate(() => [1, 3, 4].map((i) => {
      const cell = document.querySelectorAll('th')[i], r = cell.getBoundingClientRect();
      const range = document.createRange(); range.selectNodeContents(cell);
      return [range.getBoundingClientRect().right + 22, r.top + r.height / 2];
    })) },
];

(async () => {
  const browser = await chromium.launch();
  for (const lang of langs.split(',')) {
    await withDirector(repo, lang, async (url) => {
      const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, locale: lang, deviceScaleFactor: 2 });
      await page.goto(url); await page.waitForTimeout(3000);
      for (const { name, tab, clip, marks } of CLOSEUPS) {
        await page.locator('header button').nth(tab).click(); await page.waitForTimeout(1500);
        const png = path.join(OUT, `${name}-${lang}.png`);
        await page.screenshot({ path: png, clip });
        execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', png, '-quality', '88', png.replace('.png', '.webp')]);
        fs.rmSync(png);
        const at = (await marks(page)).map(([x, y]) => [+(((x - clip.x) / clip.width) * 100).toFixed(1), +(((y - clip.y) / clip.height) * 100).toFixed(1)]);
        fs.writeFileSync(path.join(OUT, `${name}-${lang}.json`), JSON.stringify({ marks: at }) + '\n');
        console.log(`img/closeups/${name}-${lang}.webp`);
      }
      await page.close();
    });
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });

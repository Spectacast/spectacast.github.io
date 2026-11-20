// The website's close-ups of Spectacast Director: one region of a page, sharp, in every language.
//   node tools/visuals/closeups-director.js <director repo, npm installed> [en,de,es,it] [close-up names]
const { chromium } = require('playwright');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const { withDirector } = require('./director-demo');

const [repo, langs = 'en,de,es,it', only = ''] = process.argv.slice(2);
if (!repo) throw new Error('usage: closeups-director.js <director repo> [languages]');
const OUT = path.join(__dirname, '..', '..', 'img', 'closeups');
fs.mkdirSync(OUT, { recursive: true });

// tab: the place of the page's tab in the header (0 is Panels); clip: the region, in page pixels at 1600 wide;
// marks: where the numbered marks go, in page pixels. The hall's are fixed (its strip is laid out the same in every
// language); the fleet's are read from the page, because its columns move with the words.
// The end of an element's own words (not of its box), and its middle line: where a mark sits beside a title.
const afterWords = (page, selector, nth, gap = 20) => page.evaluate(([selector, nth, gap]) => {
  const el = document.querySelectorAll(selector)[nth], range = document.createRange();
  range.selectNodeContents(el.firstChild.nodeType === 3 ? el.firstChild : el);
  const r = range.getBoundingClientRect();
  return [gap < 0 ? r.left + gap : r.right + gap, r.top + r.height / 2];   // a negative gap: before the words
}, [selector, nth, gap]);
/** After everything written on the line of a title: the title and the hint beside it. */
const afterLine = (page, selector, nth, gap = 22) => page.evaluate(([selector, nth, gap]) => {
  const el = document.querySelectorAll(selector)[nth], range = document.createRange();
  range.selectNodeContents(el.parentElement.children.length > 1 && el.parentElement.getBoundingClientRect().height < 40 ? el.parentElement : el);
  const r = range.getBoundingClientRect(), t = el.getBoundingClientRect();
  return [r.right + gap, t.top + t.height / 2];
}, [selector, nth, gap]);
const box = (locator) => locator.first().boundingBox();
// The bordered box an editor sits in: card(element), available inside the page.
const CARD = `window.card = (el) => { let c = el.parentElement; while (c.parentElement && (getComputedStyle(c).borderTopWidth === '0px' || c.getBoundingClientRect().width < 700)) c = c.parentElement; return c; };`;
const TITLES = 'h3.uppercase';   // the small titles inside Director's editors

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

  // How things are built. The panel editor: the ready-made blocks, an empty cell, Save.
  { name: 'director-build-panel', tab: 0,
    prepare: async (page) => {
      // Edit is the last button of the row of panel names.
      const row = await page.evaluate(() => [...document.querySelectorAll('button')].map((b, i) => [i, b.getBoundingClientRect()])
        .filter(([, r]) => r.top > 80 && r.top < 100).sort((a, b) => a[1].left - b[1].left).map(([i]) => i));
      await page.locator('button').nth(row[row.length - 1]).click(); await page.waitForTimeout(1200);
    },
    at: async (page) => {
      const places = await page.evaluate(() => {
        const rect = (e) => { const r = e.getBoundingClientRect(); return { x: r.left, y: r.top, w: r.width, h: r.height, t: e.textContent.trim() }; };
        const row = (lo, hi, sel) => [...document.querySelectorAll(sel)].map(rect).filter((r) => r.y > lo && r.y < hi && r.w > 0).sort((a, b) => a.x - b.x);
        const label = row(85, 110, 'span').filter((r) => r.t && r.x > 500)[0];          // "blocks"
        const save = row(115, 140, 'button').filter((r) => r.x > 1200)[0];               // Save, left of Discard
        const cell = row(330, 430, 'button').filter((r) => r.t === '+' && r.x > 1380)[0];  // an empty cell
        return { label, save, cell };
      });
      const x = places.label.x - 56;
      return { clip: { x, y: 78, width: 1600 - x, height: 392 },
        marks: [[places.label.x - 24, places.label.y + places.label.h / 2], [places.cell.x + places.cell.w / 2, places.cell.y + places.cell.h / 2], [places.save.x - 18, places.save.y + places.save.h / 2]] };
    } },
  // The rule editor with the "active speaker" template opened: when, only if, then.
  { name: 'director-build-rule', tab: 3,
    prepare: async (page) => {
      // "+ from template" is the last button of the bar at the top of the page.
      const plus = await page.evaluate(() => [...document.querySelectorAll('button')].map((b, i) => [i, b.getBoundingClientRect(), b.textContent.trim()])
        .filter(([, r, t]) => t.startsWith('+') && r.top > 100 && r.top < 135).sort((a, b) => a[1].left - b[1].left).map(([i]) => i));
      await page.locator('button').nth(plus[plus.length - 1]).click(); await page.waitForTimeout(600);
      const pick = page.locator('select').filter({ has: page.locator('option', { hasText: '→' }) }).first();
      await pick.selectOption({ index: 2 }); await page.waitForTimeout(400);
      await pick.locator('xpath=ancestor::*[.//button][1]').locator('button').first().click(); await page.waitForTimeout(1000);
    },
    at: async (page) => {
      const card = await page.evaluate((sel) => {
        const r = card(document.querySelector(sel)).getBoundingClientRect(); return { x: r.left, y: r.top, width: r.width, height: r.height };
      }, TITLES);
      return { clip: { x: card.x - 10, y: card.y - 10, width: card.width + 20, height: card.height + 20 },
        marks: [await afterWords(page, TITLES, 0), await afterWords(page, TITLES, 1), await afterWords(page, TITLES, 2)] };
    } },
  // A driver without code: the example OSC driver imported and opened: how it talks, what each device needs, its commands.
  { name: 'director-build-driver', tab: 6,
    prepare: async (page) => {
      await page.locator('label input[type=file][accept*=json]').last().setInputFiles(path.join(__dirname, '..', '..', 'examples', 'drivers', 'generic-osc.json'));
      await page.waitForTimeout(1200);
      // try, Edit, export, delete: the second button on the driver's line.
      const line = await box(page.getByText('oscdevice', { exact: true }));
      const buttons = await page.evaluate((y) => [...document.querySelectorAll('button')].map((b, i) => [i, b.getBoundingClientRect()])
        .filter(([, r]) => Math.abs(r.top + r.height / 2 - y) < 24).sort((a, b) => a[1].left - b[1].left).map(([i]) => i), line.y + line.height / 2);
      await page.locator('button').nth(buttons[1]).click(); await page.waitForTimeout(1000);
    },
    at: async (page) => {
      const transport = page.locator('select').filter({ has: page.locator('option', { hasText: 'OSC (UDP)' }) }).first();
      const label = await page.evaluate((el) => {
        const l = el.closest('label'), range = document.createRange(); range.selectNodeContents([...l.childNodes].find((n) => n.textContent.trim() && n !== el) || l);
        const r = range.getBoundingClientRect(); return [r.left - 26, r.top + r.height / 2];
      }, await transport.elementHandle());
      const card = await page.evaluate((sel) => {
        const r = card(document.querySelector(sel)).getBoundingClientRect(); return { x: r.left, y: r.top, width: r.width };
      }, TITLES);
      return { clip: { x: card.x - 10, y: card.y - 10, width: card.width + 20, height: 560 },
        marks: [label, await afterLine(page, TITLES, 0), await afterLine(page, TITLES, 1)] };
    } },
];

(async () => {
  const browser = await chromium.launch();
  for (const lang of langs.split(',')) {
    await withDirector(repo, lang, async (url) => {
      const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, locale: lang, deviceScaleFactor: 2 });
      for (const c of CLOSEUPS.filter((c) => !only || only.split(',').includes(c.name))) {
        const { name, tab } = c;
        await page.goto(url); await page.waitForTimeout(2500);   // each from a fresh page
        await page.locator('header button').nth(tab).click(); await page.waitForTimeout(1500);
        if (c.prepare) await c.prepare(page);
        await page.evaluate(CARD);
        // An example in an empty field names an internal address: keep the example, without that part.
        await page.evaluate(() => document.querySelectorAll('[placeholder*="zoomdirector"]').forEach((i) => { i.placeholder = i.placeholder.split(' && ')[0]; }));
        const { clip, marks } = c.at ? await c.at(page) : { clip: c.clip, marks: await c.marks(page) };
        const png = path.join(OUT, `${name}-${lang}.png`);
        await page.screenshot({ path: png, clip });
        execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', png, '-quality', '88', png.replace('.png', '.webp')]);
        fs.rmSync(png);
        const at = marks.map(([x, y]) => [+(((x - clip.x) / clip.width) * 100).toFixed(1), +(((y - clip.y) / clip.height) * 100).toFixed(1)]);
        fs.writeFileSync(path.join(OUT, `${name}-${lang}.json`), JSON.stringify({ marks: at }) + '\n');
        console.log(`img/closeups/${name}-${lang}.webp`);
      }
      await page.close();
    });
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });

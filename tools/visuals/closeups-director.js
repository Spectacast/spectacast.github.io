// The website's close-ups of Spectacast Director: one region of a page, sharp, in every language.
//   node tools/visuals/closeups-director.js <director repo, npm installed> [en,de,es,it] [close-up names]
const { chromium } = require('playwright');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const { withDirector } = require('./director-demo');

const [repo, langs = 'en,de,es,it', only = ''] = process.argv.slice(2);
if (!repo) throw new Error('usage: closeups-director.js <director repo> [languages] [close-up names]');
const OUT = process.env.OUT || path.join(__dirname, '..', '..', 'img', 'closeups');
fs.mkdirSync(OUT, { recursive: true });

// A close-up: tab is the place of the page's tab in the header (0 is Panels); prepare opens what is to be shown, in the
// wide window; view, if given, is the window the picture is taken in (the editors are taken narrow, so their text is
// large on the website); at gives the region (clip) and the marks, in page pixels.
// A mark is [x, y] for its middle, or [x, y, 'after' | 'before'] for a mark beside words that end or start there:
// the website keeps it clear of the words at every size the picture is shown (site.css, .cu-mark).

/** Where an element's words end (not its box), on their middle line: only its own first words, or all of them. */
const endOf = (page, selector, nth, all = false) => page.evaluate(([selector, nth, all]) => {
  const el = document.querySelectorAll(selector)[nth], range = document.createRange();
  range.selectNodeContents(!all && el.firstChild.nodeType === 3 ? el.firstChild : el);
  const r = range.getBoundingClientRect();
  if (r.height > 30) throw new Error('the words of ' + selector + ' ' + nth + ' are on more than one line');
  return [r.right, r.top + r.height / 2, 'after'];
}, [selector, nth, all]);
const rect = (page, selector, nth = 0) => page.evaluate(([selector, nth]) => {
  const r = document.querySelectorAll(selector)[nth].getBoundingClientRect(); return { x: r.left, y: r.top, width: r.width, height: r.height };
}, [selector, nth]);
const box = (locator) => locator.first().boundingBox();
// The bordered box an editor sits in: card(element), available inside the page.
const CARD = `window.card = (el) => { let c = el.parentElement; while (c.parentElement && (getComputedStyle(c).borderTopWidth === '0px' || c.getBoundingClientRect().width < 700)) c = c.parentElement; return c; };`;
const cardOf = (page, selector) => page.evaluate((selector) => {
  const r = card(document.querySelector(selector)).getBoundingClientRect(); return { x: r.left, y: r.top, width: r.width, height: r.height };
}, selector);
const TITLES = 'h3.uppercase';   // the small titles inside Director's editors
const NARROW = { width: 800, height: 1100 };
// Never in a picture: internal names, the congress the software grew up at, addresses of real machines.
const BANNED = 'zoomdirector|fake|laparoscopic|\\b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\b';

const CLOSEUPS = [
  // The hall's marks are fixed: its strip is laid out the same in every language.
  { name: 'director-hall', tab: 0,
    at: async () => ({ clip: { x: 240, y: 192, width: 452, height: 312 }, marks: [[446, 220], [446, 258], [446, 429]] }) },
  // Beside the titles of the helper, users and waiting columns, which move with the words.
  { name: 'director-fleet', tab: 2,
    at: async (page) => ({ clip: { x: 160, y: 120, width: 760, height: 198 }, marks: await page.evaluate(() => [1, 3, 4].map((i) => {
      const cell = document.querySelectorAll('th')[i], r = cell.getBoundingClientRect();
      const range = document.createRange(); range.selectNodeContents(cell);
      return [range.getBoundingClientRect().right + 22, r.top + r.height / 2];
    })) }) },

  // How things are built. The panel editor: the ready-made blocks, an empty cell, Save.
  { name: 'director-build-panel', tab: 0, view: NARROW,
    prepare: async (page) => {
      // Edit is the last button of the row of panel names.
      const row = await page.evaluate(() => [...document.querySelectorAll('button')].map((b, i) => [i, b.getBoundingClientRect()])
        .filter(([, r]) => r.top > 80 && r.top < 100).sort((a, b) => a[1].left - b[1].left).map(([i]) => i));
      await page.locator('button').nth(row[row.length - 1]).click(); await page.waitForTimeout(1200);
    },
    at: async (page) => {
      // The first empty cell is beyond the right edge of a narrow window: bring it in, as an operator would by scrolling.
      await page.evaluate(() => {
        let e = [...document.querySelectorAll('button.border-dashed')].filter((b) => b.textContent.trim() === '+')[0];
        while (e && !(e.scrollWidth > e.clientWidth + 40 && /auto|scroll/.test(getComputedStyle(e).overflowX))) e = e.parentElement;
        if (e) e.scrollLeft = 360;   // four cells: the strip's own title, at its left end, is out of the picture whole
      });
      await page.waitForTimeout(500);
      const p = await page.evaluate(() => {
        const r = (e) => { const b = e.getBoundingClientRect(); return { x: b.left, y: b.top, w: b.width, h: b.height, right: b.right, bottom: b.bottom }; };
        const save = r(document.querySelector('span.ml-auto button.bg-emerald-600'));
        const label = r(document.querySelector('span.ml-2.uppercase'));                  // "blocks"
        const dashed = [...document.querySelectorAll('button.border-dashed')];
        const chips = dashed.map(r).filter((c) => c.y < save.bottom);                    // the blocks, and "+ block" last
        // The first empty cell of the panel that can be seen whole: not one under a control, not one inside a block.
        const seen = (b) => { const q = b.getBoundingClientRect(); return q.left > 200 && q.right < 780 && b.contains(document.elementFromPoint(q.left + q.width / 2, q.top + q.height / 2)); };
        const cell = r(dashed.filter((b) => b.textContent.trim() === '+' && b.getBoundingClientRect().top > save.bottom && seen(b))[0]);
        return { save, label, last: chips[chips.length - 1], cell };
      });
      // After the last block there must be room for a mark before Save, when both are on one line.
      if (Math.abs(p.last.y - p.save.y) < 10 && p.save.x - p.last.right < 110) throw new Error('no room for two marks between the blocks and Save');
      return { clip: { x: 6, y: p.label.y - 16, width: 788, height: p.cell.bottom + 96 - (p.label.y - 16) },
        marks: [[p.last.right, p.last.y + p.last.h / 2, 'after'], [p.cell.right - 2, p.cell.bottom - 2], [p.save.x, p.save.y + p.save.h / 2, 'before']] };
    } },
  // The rule editor with a ready-made rule in it: when, only if, then.
  { name: 'director-build-rule', tab: 3, view: NARROW,
    prepare: async (page) => {
      // "+ from template" is the last button of the bar at the top of the page.
      const plus = await page.evaluate(() => [...document.querySelectorAll('button')].map((b, i) => [i, b.getBoundingClientRect(), b.textContent.trim()])
        .filter(([, r, t]) => t.startsWith('+') && r.top > 100 && r.top < 135).sort((a, b) => a[1].left - b[1].left).map(([i]) => i));
      await page.locator('button').nth(plus[plus.length - 1]).click(); await page.waitForTimeout(600);
      const pick = page.locator('select').filter({ has: page.locator('option[value=followSpeaker]') }).first();
      await pick.selectOption('followSpeaker'); await page.waitForTimeout(400);   // Active speaker → scene, with hold time
      await pick.locator('xpath=ancestor::*[.//button][1]').locator('button').first().click(); await page.waitForTimeout(1000);
    },
    at: async (page) => {
      const card = await cardOf(page, TITLES);
      return { clip: { x: card.x - 8, y: card.y - 8, width: card.width + 16, height: card.height + 16 },
        marks: [await endOf(page, TITLES, 0), await endOf(page, TITLES, 1), await endOf(page, TITLES, 2)] };
    } },
  // A driver without code: the example OSC driver imported and opened: how it talks, what each device needs, its commands.
  { name: 'director-build-driver', tab: 6, view: NARROW,
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
      // After the word above the transport list.
      const label = await page.evaluate((el) => {
        const l = el.closest('label'), range = document.createRange(); range.selectNodeContents([...l.childNodes].find((n) => n.textContent.trim() && n !== el) || l);
        const r = range.getBoundingClientRect(); return [r.right, r.top + r.height / 2, 'after'];
      }, await transport.elementHandle());
      const card = await cardOf(page, TITLES);
      // Down to the end of the first command, so no line of text is cut through.
      const bottom = await page.evaluate((sel) => {
        let c = document.querySelectorAll(sel)[1].nextElementSibling;
        if (c.getBoundingClientRect().height > 400 && c.firstElementChild) c = c.firstElementChild;
        return c.getBoundingClientRect().bottom;
      }, TITLES);
      return { clip: { x: card.x - 8, y: card.y - 8, width: card.width + 16, height: bottom + 10 - (card.y - 8) },
        marks: [label, await endOf(page, TITLES, 0, true), await endOf(page, TITLES, 1, true)] };
    } },
];

(async () => {
  const browser = await chromium.launch();
  for (const lang of langs.split(',')) {
    await withDirector(repo, lang, async (url) => {
      for (const c of CLOSEUPS.filter((c) => !only || only.split(',').includes(c.name))) {
        const { name, tab } = c;
        const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, locale: lang, deviceScaleFactor: 2 });
        await page.goto(url); await page.waitForTimeout(2500);
        await page.locator('header button').nth(tab).click(); await page.waitForTimeout(1500);
        if (c.prepare) await c.prepare(page);
        if (c.view) { await page.setViewportSize(c.view); await page.waitForTimeout(800); }
        await page.mouse.move(0, 0);   // nothing in the picture is lit by hovering
        await page.evaluate(CARD);
        // An example in an empty field names an internal address: keep the example, without that part.
        await page.evaluate(() => document.querySelectorAll('[placeholder*="zoomdirector"]').forEach((i) => { i.placeholder = i.placeholder.split(' && ')[0]; }));
        const { clip, marks } = await c.at(page);
        const view = page.viewportSize();
        if (clip.x < 0 || clip.y < 0 || clip.x + clip.width > view.width || clip.y + clip.height > view.height) throw new Error(`${name}-${lang}: the region ${JSON.stringify(clip)} does not fit the window`);
        // What can be read inside the region: text, and what fields hold or suggest.
        const found = await page.evaluate(([clip, banned]) => {
          const inside = (r) => r.width && r.right > clip.x && r.left < clip.x + clip.width && r.bottom > clip.y && r.top < clip.y + clip.height;
          const words = [], walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT), range = document.createRange();
          for (let n = walker.nextNode(); n; n = walker.nextNode()) { range.selectNodeContents(n); if (n.textContent.trim() && inside(range.getBoundingClientRect())) words.push(n.textContent); }
          for (const f of document.querySelectorAll('input, textarea, select')) if (inside(f.getBoundingClientRect())) words.push(f.value || '', f.placeholder || '', f.selectedOptions ? [...f.selectedOptions].map((o) => o.textContent).join(' ') : '');
          return words.filter((w) => new RegExp(banned, 'i').test(w));
        }, [clip, BANNED]);
        if (found.length) throw new Error(`${name}-${lang}: the picture would show ${JSON.stringify(found.slice(0, 5))}`);
        const png = path.join(OUT, `${name}-${lang}.png`);
        await page.screenshot({ path: png, clip });
        execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', png, '-quality', '88', png.replace('.png', '.webp')]);
        fs.rmSync(png);
        const at = marks.map(([x, y, side]) => [+(((x - clip.x) / clip.width) * 100).toFixed(1), +(((y - clip.y) / clip.height) * 100).toFixed(1), ...(side ? [side] : [])]);
        for (const [x, y, side] of at) if (x < 2 || y < 2 || y > 98 || x > (side === 'after' ? 93 : 98) || (side === 'before' && x < 7)) throw new Error(`${name}-${lang}: a mark at ${x} %, ${y} % would leave the picture`);
        fs.writeFileSync(path.join(OUT, `${name}-${lang}.json`), JSON.stringify({ marks: at }) + '\n');
        // The picture for link previews is made from this one by src/build.py, when there is none.
        fs.rmSync(path.join(OUT, '..', 'og', `${name}-${lang}.jpg`), { force: true });
        console.log(`img/closeups/${name}-${lang}.webp ${Math.round(clip.width)} x ${Math.round(clip.height)} ${JSON.stringify(at)}`);
        await page.close();
      }
    });
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });

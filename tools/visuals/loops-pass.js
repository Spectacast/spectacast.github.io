// The website's loops of Spectacast Pass, recorded from the Demo Congress 2027 in every language.
//   node tools/visuals/loops-pass.js <pass repo, npm installed> [en,de,es,it] [loop names]
// The door app and the Live page are the real pages, side by side on one stage; only the paper badge is drawn.
// The Live page is cut to its rooms and its latest scans: the door phones between them are left out of the picture.
const { chromium } = require('playwright');
const path = require('node:path');
const { withPass } = require('./pass-demo');
const { Recorder } = require('./record');

const [repo, langs = 'en,de,es,it', only = ''] = process.argv.slice(2);
if (!repo) throw new Error('usage: loops-pass.js <pass repo> [languages] [loops]');
const OUT = process.env.OUT || path.join(__dirname, '..', '..', 'img', 'loops');
const LOCALE = { en: 'en-GB', de: 'de-DE', es: 'es-ES', it: 'it-IT' };

/** A phone on the left with the door app, the Live page on the right. */
const stage = (base, info) => `<!doctype html><meta charset="utf-8"><style>
  html, body { margin: 0; background: #f3f1ea; font-family: Inter, system-ui, sans-serif; }
  #stage { position: relative; width: 1120px; height: 620px; overflow: hidden; }
  #phone { position: absolute; left: 36px; top: 26px; width: 292px; height: 568px; border-radius: 34px; background: #111318; box-shadow: 0 18px 40px rgba(17,19,24,.28); }
  #phone div { position: absolute; inset: 10px; border-radius: 25px; overflow: hidden; background: #fff; }
  #phone iframe { width: 390px; height: 786px; border: 0; transform: scale(${272 / 390}); transform-origin: 0 0; }
  #desk { position: absolute; left: 372px; top: 44px; width: 716px; height: 532px; border-radius: 14px; overflow: hidden; background: #f3f1ea; border: 1px solid #dcd8cc; box-shadow: 0 18px 40px rgba(17,19,24,.16); }
  #desk iframe { width: 960px; height: 800px; border: 0; margin-top: -66px; transform: scale(${716 / 960}); transform-origin: 0 0; }
  #badge { position: absolute; left: 110px; top: 640px; width: 150px; height: 196px; border-radius: 10px; background: #fff; box-shadow: 0 10px 30px rgba(17,19,24,.35); text-align: center; font-size: 13px; color: #111318; }
  #badge i { display: block; height: 18px; border-radius: 10px 10px 0 0; background: #7a4e9b; }
  #badge b { display: block; margin: 9px 0 1px; font-size: 15px; }
  #badge span { display: block; font-size: 11px; letter-spacing: .08em; color: #7a4e9b; font-weight: 700; }
  #badge svg { width: 84px; height: 84px; margin-top: 8px; }
</style><div id="stage">
  <div id="phone"><div><iframe id="door" src="${base}/scan?event=${info.event}&door=${info.door}&name=${encodeURIComponent(info.doorName)}"></iframe></div></div>
  <div id="desk"><iframe id="live" src="${base}/"></iframe></div>
  <div id="badge"><i></i><b>Sofia Navarro</b><span>${info.label}</span><svg viewBox="0 0 21 21" shape-rendering="crispEdges">${qr()}</svg></div>
</div>`;

/** A picture of a QR code: the three corner squares and a fixed scatter, not a code that reads. */
function qr() {
  let s = 7, cells = '';
  const eye = (x, y) => `<rect x="${x}" y="${y}" width="7" height="7"/><rect x="${x + 1}" y="${y + 1}" width="5" height="5" fill="#fff"/><rect x="${x + 2}" y="${y + 2}" width="3" height="3"/>`;
  for (let y = 0; y < 21; y++) for (let x = 0; x < 21; x++) {
    s = (s * 1103515245 + 12345) % 2147483648;
    const corner = (x < 8 && y < 8) || (x > 12 && y < 8) || (x < 8 && y > 12);
    if (!corner && s / 2147483648 < 0.48) cells += `<rect x="${x}" y="${y}" width="1" height="1"/>`;
  }
  return `<g fill="#111318">${cells}${eye(0, 0)}${eye(14, 0)}${eye(0, 14)}</g>`;
}

const LOOPS = {
  // A badge at the door: the phone answers in green, and the room's count goes up on the Live page.
  'pass-scan': async (page, { base, info }) => {
    // The stage is served from the hub's own address, so the door app runs as it does on a phone (a secure page).
    await page.route(base + '/__stage', (route) => route.fulfill({ contentType: 'text/html', body: stage(base, info) }));
    await page.goto(base + '/__stage');
    const door = await (await page.$('#door')).contentFrame(), live = await (await page.$('#live')).contentFrame();
    await live.waitForSelector('nav button'); await page.waitForTimeout(800);
    const tab = live.locator('nav button').nth(4);   // Setup, Attendees, Rules, Upload scans, Live
    await tab.dispatchEvent('click');   // from inside the frame: the tabs are above the part the stage shows
    await live.waitForSelector('.room');
    await live.addStyleTag({ content: '#content > h2:nth-of-type(2), #content > h2:nth-of-type(2) + * { display: none; }' });
    // Start the picture at "Rooms now", wherever the header above it ends in this language.
    const top = await live.evaluate(() => document.querySelector('#content h2').getBoundingClientRect().top);
    await page.evaluate((y) => { document.getElementById('live').style.marginTop = -Math.round((y - 26) * 716 / 960) + 'px'; }, top);
    await page.waitForTimeout(600);
    const rec = new Recorder(page, { x: 0, y: 0, width: 1120, height: 620 });
    rec.pointer = false;
    await rec.start(); await rec.hold(900);
    // The badge comes up to the phone's camera.
    for (let i = 1; i <= 14; i++) {
      const k = i / 14, e = 1 - Math.pow(1 - k, 3);
      await page.evaluate((top) => { document.getElementById('badge').style.top = top + 'px'; }, 640 - 400 * e);
      await rec.frame(40);
    }
    await rec.hold(350);
    await door.evaluate(() => window.focus());
    await page.keyboard.type(info.guest, { delay: 5 }); await page.keyboard.press('Enter');
    await page.waitForTimeout(500);
    await rec.hold(500);
    for (let i = 1; i <= 10; i++) {
      await page.evaluate((top) => { document.getElementById('badge').style.top = top + 'px'; }, 240 + 420 * (i / 10) * (i / 10));
      await rec.frame(40);
    }
    await rec.hold(500);
    await tab.dispatchEvent('click'); await page.waitForTimeout(500);   // the Live page asks again every 5 seconds: here, now
    await rec.hold(3200);
    return rec;
  },
};

(async () => {
  const browser = await chromium.launch();
  for (const lang of langs.split(',')) {
    for (const name of Object.keys(LOOPS).filter((n) => !only || only.split(',').includes(n))) {
      await withPass(repo, lang, async (pass) => {
        const ctx = await browser.newContext({ viewport: { width: 1120, height: 620 }, deviceScaleFactor: 2, colorScheme: 'light', timezoneId: 'Europe/Berlin', locale: LOCALE[lang] });
        const page = await ctx.newPage();
        await page.clock.setFixedTime(new Date(pass.info.snapshotAt));
        const rec = await LOOPS[name](page, pass);
        const info = await rec.save(path.join(OUT, `${name}-${lang}`), 1280);
        console.log(`${name}-${lang}: ${info.seconds.toFixed(1)} s, webm ${Math.round(info.webm / 1024)} KB, mp4 ${Math.round(info.mp4 / 1024)} KB`);
        await ctx.close();
      });
    }
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });

// Screenshots of Spectacast Pass with the Demo Congress 2027, for the website.
//   node tools/screenshots/shot-pass.js <pass repo> <output folder>
// Seeds a fresh database, starts the hub on port 4899, sets the browser clock to 15:31 in Berlin and
// takes each page in light and dark.
const { chromium } = require('playwright');
const { execFileSync, spawn } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const [passRepo, out] = process.argv.slice(2);
if (!passRepo || !out) throw new Error('usage: shot-pass.js <pass repo> <output folder>');
fs.mkdirSync(out, { recursive: true });
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'pass-demo-'));
const db = path.join(tmp, 'demo.db');
const node = ['--disable-warning=ExperimentalWarning'];
const info = JSON.parse(execFileSync('node', [...node, path.join(__dirname, 'seed-pass.ts'), passRepo, db]).toString());
const hub = spawn('node', [...node, 'src/main.ts', '--db', db, '--port', '4899', '--https-port', '0'], { cwd: passRepo, stdio: 'ignore' });
const base = 'http://localhost:4899';

(async () => {
  for (let i = 0; i < 50; i++) { try { await fetch(base + '/api/events'); break; } catch { await new Promise((r) => setTimeout(r, 200)); } }
  const b = await chromium.launch();
  const when = new Date(info.snapshotAt);
  for (const scheme of ['light', 'dark']) {
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, colorScheme: scheme, timezoneId: 'Europe/Berlin', locale: 'en-GB' });
    const pg = await ctx.newPage();
    await pg.clock.setFixedTime(when);
    await pg.goto(base + '/'); await pg.waitForTimeout(1000);
    for (const tab of ['Setup', 'Attendees', 'Live', 'Reports', 'Rules', 'Certificates']) {
      await pg.getByRole('button', { name: tab, exact: true }).first().click(); await pg.waitForTimeout(1000);
      await pg.screenshot({ path: `${out}/pass-${tab.toLowerCase()}-${scheme}.png` });
    }
    // The door app on a phone: idle, then a badge read by a keyboard scanner.
    const phone = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, colorScheme: scheme, timezoneId: 'Europe/Berlin' });
    const ph = await phone.newPage();
    await ph.clock.setFixedTime(when);
    await ph.goto(`${base}/scan?event=${info.event}&door=${info.door}&name=Hall%20A%20door`); await ph.waitForTimeout(1500);
    await ph.screenshot({ path: `${out}/pass-door-idle-${scheme}.png` });
    await ph.keyboard.type(info.guest, { delay: 5 }); await ph.keyboard.press('Enter'); await ph.waitForTimeout(700);
    await ph.screenshot({ path: `${out}/pass-door-welcome-${scheme}.png` });
    await phone.close();
    await ctx.close();
  }
  await b.close();
  hub.kill();
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('Pass screenshots in', out);
})().catch((e) => { hub.kill(); console.error(e); process.exit(1); });

// Screenshots of Spectacast Director for the website: a four-room show built by the Director's own
// generator, run against stand-in Zoom Directors and OBS (the Director's scripts/channels-demo.ts),
// with invented speaker names. Nothing reaches a real machine.
//   node tools/screenshots/shot-director.js <director repo, npm installed> <output folder>
const { chromium } = require('playwright');
const { execFileSync, spawn } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const [repo, out] = process.argv.slice(2);
if (!repo || !out) throw new Error('usage: shot-director.js <director repo> <output folder>');
fs.mkdirSync(out, { recursive: true });
const work = fs.mkdtempSync(path.join(repo, 'shows', 'site-demo-'));
const node = ['--disable-warning=ExperimentalWarning'];

// Four PCs, as the generator's input.
const rooms = ['A', 'B', 'C', 'D'];
const pcs = { version: 1, name: 'Demo Congress 2027', devices: [
  ...rooms.flatMap((r, i) => [
    { id: `zoom${r}`, driver: 'zoomdirector', name: `Zoom ${r}`, config: { host: `192.168.1.${11 + i}` } },
    { id: `obs${r}`, driver: 'obs', name: `OBS ${r}`, config: { url: `ws://192.168.1.${11 + i}:4455`, passwordEnv: 'OBS_PASSWORD' } },
  ]),
  { id: 'ndi', driver: 'ndi', name: 'NDI', config: {} },
] };
fs.writeFileSync(path.join(work, 'pcs.json'), JSON.stringify(pcs));
const NAMES = { en: 'Hall A,Hall B,Hall C,Workshop', de: 'Saal A,Saal B,Saal C,Workshop',
  es: 'Sala A,Sala B,Sala C,Taller', it: 'Sala A,Sala B,Sala C,Workshop' };
for (const lang of Object.keys(NAMES))
  execFileSync('node', [...node, 'scripts/channels-show.ts', '--in', path.join(work, 'pcs.json'), '--out', path.join(work, `show.${lang}.json`),
    '--channels', rooms.map((r) => `zoom${r}:obs${r}`).join(','), '--channel-names', NAMES[lang],
    '--wall', '2:1,2', ...(lang === 'en' ? [] : ['--show-language', lang])], { cwd: repo, stdio: 'ignore' });

// The demo runner with invented guests in place of its test names.
const demo = fs.readFileSync(path.join(repo, 'scripts/channels-demo.ts'), 'utf8')
  .replace(/const GUESTS = \[[^\]]*\];/, "const GUESTS = ['Dr. Elena Ortega', 'Prof. Jonas Weber', 'Dr. Chiara Fontana', 'Dr. Mateo Serrano', 'Dr. Lena Hartmann', 'Prof. Davide Greco'];")
  .replace("name: 'bob'", "name: 'Dr. Nils Brandt'")
  // A different panel of speakers in each room.
  .replace('GUESTS.slice(0, 2 + fakes.length)', '[...GUESTS.slice(fakes.length), ...GUESTS.slice(0, fakes.length)].slice(0, 2 + fakes.length)');
const runner = path.join(repo, 'scripts', `.site-demo-${process.pid}.ts`);
fs.writeFileSync(runner, demo);
let engine = null;
const startEngine = (lang) => {
  engine = spawn('node', [...node, runner, '--show', path.join(work, `show.${lang}.json`), '--out', path.join(work, 'run.json'), '--port', '4720', '--listen-port', '12441'], { cwd: repo, stdio: 'ignore' });
  return new Promise((r) => setTimeout(r, 3000));
};
const web = spawn('npm', ['exec', '-w', 'apps/web', '--', 'vite', '--port', '4721', '--strictPort'], { cwd: repo, stdio: 'ignore', env: { ...process.env, ENGINE_URL: 'http://127.0.0.1:4720' } });
const stop = () => { engine?.kill(); web.kill(); fs.rmSync(runner, { force: true }); fs.rmSync(work, { recursive: true, force: true }); };

(async () => {
  for (let i = 0; i < 100; i++) { try { if ((await fetch('http://127.0.0.1:4721/')).ok) break; } catch {} await new Promise((r) => setTimeout(r, 200)); }
  await new Promise((r) => setTimeout(r, 2500));
  const b = await chromium.launch();
  for (const lang of ['en', 'de', 'es', 'it']) {
    await startEngine(lang);
    const pg = await b.newPage({ viewport: { width: 1600, height: 1000 }, locale: lang });
    await pg.goto('http://127.0.0.1:4721/'); await pg.waitForTimeout(2500);
    await pg.screenshot({ path: `${out}/director-panels-${lang}.png` });
    await pg.locator('button:has-text("left_panel_close")').first().click(); await pg.waitForTimeout(800);
    await pg.screenshot({ path: `${out}/director-channels-${lang}.png` });
    if (lang === 'en') {
      for (const [i, name] of ['wall', 'fleet', 'rules', 'devices'].entries()) {
        await pg.locator('header button').nth(i + 1).click(); await pg.waitForTimeout(1500);
        // The fleet is a short table: no need for the empty page under it.
        await pg.screenshot({ path: `${out}/director-${name}-en.png`, ...(name === 'fleet' ? { clip: { x: 0, y: 0, width: 1600, height: 420 } } : {}) });
      }
    }
    await pg.close();
    engine.kill(); await new Promise((r) => setTimeout(r, 800));
  }
  await b.close();
  stop();
  console.log('Director screenshots in', out);
})().catch((e) => { stop(); console.error(e); process.exit(1); });

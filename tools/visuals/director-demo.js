// Spectacast Director running the invented Demo Congress 2027 against stand-in devices (the Director's own
// scripts/channels-demo.ts), for the website's loops and close-ups. Nothing reaches a real machine.
//   const { withDirector } = require('./director-demo');
//   await withDirector(repo, 'en', async (url, cue) => { ...a browser opens url; cue('wait', 'Dr. …') stages an arrival... });
const { execFileSync, spawn } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const NAMES = { en: 'Hall A,Hall B,Hall C,Workshop', de: 'Saal A,Saal B,Saal C,Workshop',
  es: 'Sala A,Sala B,Sala C,Taller', it: 'Sala A,Sala B,Sala C,Workshop' };
const node = ['--disable-warning=ExperimentalWarning'];
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function withDirector(repo, lang, fn) {
  const work = fs.mkdtempSync(path.join(repo, 'shows', 'site-demo-'));
  const rooms = ['A', 'B', 'C', 'D'];
  const pcs = { version: 1, name: 'Demo Congress 2027', devices: [
    ...rooms.flatMap((r, i) => [
      { id: `zoom${r}`, driver: 'zoomdirector', name: `Zoom ${r}`, config: { host: `192.168.1.${11 + i}` } },
      { id: `obs${r}`, driver: 'obs', name: `OBS ${r}`, config: { url: `ws://192.168.1.${11 + i}:4455`, passwordEnv: 'OBS_PASSWORD' } },
    ]),
    { id: 'ndi', driver: 'ndi', name: 'NDI', config: {} },
  ] };
  fs.writeFileSync(path.join(work, 'pcs.json'), JSON.stringify(pcs));
  execFileSync('node', [...node, 'scripts/channels-show.ts', '--in', path.join(work, 'pcs.json'), '--out', path.join(work, 'show.json'),
    '--channels', rooms.map((r) => `zoom${r}:obs${r}`).join(','), '--channel-names', NAMES[lang],
    '--wall', '2:1,2', ...(lang === 'en' ? [] : ['--show-language', lang])], { cwd: repo, stdio: 'ignore' });

  // The demo runner with invented guests in place of its test names, and a way to stage what happens next:
  // a file dropped in the cue folder makes someone enter a hall's waiting room.
  const cues = path.join(work, 'cues');
  fs.mkdirSync(cues);
  // Each change must find its place: if Director's demo script moved on, stop here and not with wrong pictures.
  const swap = (text, from, to) => {
    const out = text.replace(from, to);
    if (out === text) throw new Error(`scripts/channels-demo.ts has changed: ${from} is not in it any more`);
    return out;
  };
  let demo = fs.readFileSync(path.join(repo, 'scripts/channels-demo.ts'), 'utf8');
  demo = swap(demo, /const GUESTS = \[[^\]]*\];/, "const GUESTS = ['Dr. Elena Ortega', 'Prof. Jonas Weber', 'Dr. Chiara Fontana', 'Dr. Mateo Serrano', 'Dr. Lena Hartmann', 'Prof. Davide Greco'];");
  demo = swap(demo, "name: 'bob'", "name: 'Dr. Nils Brandt'");
  demo = swap(demo, 'GUESTS.slice(0, 2 + fakes.length)', '[...GUESTS.slice(fakes.length), ...GUESTS.slice(0, fakes.length)].slice(0, 2 + fakes.length)');
  demo += `
import { readdirSync, readFileSync, rmSync } from 'node:fs';
setInterval(() => {
  for (const file of readdirSync(${JSON.stringify(cues)})) {
    const cue = JSON.parse(readFileSync(${JSON.stringify(cues)} + '/' + file, 'utf8'));
    rmSync(${JSON.stringify(cues)} + '/' + file);
    const fake = fakes[cue.hall ?? 0];
    if (cue.do === 'wait') fake.enterWaitingRoom({ zoomId: 900 + Math.floor(Math.random() * 90), pId: 'cue-' + Date.now(), name: cue.name });
  }
}, 100);
`;
  const runner = path.join(repo, 'scripts', `.site-demo-${process.pid}.ts`);
  fs.writeFileSync(runner, demo);
  let n = 0;
  const cue = (what, name, hall = 0) => fs.writeFileSync(path.join(cues, `${n++}.json`), JSON.stringify({ do: what, name, hall }));
  const engine = spawn('node', [...node, runner, '--show', path.join(work, 'show.json'), '--out', path.join(work, 'run.json'), '--port', '4720', '--listen-port', '12441'], { cwd: repo, stdio: 'ignore' });
  // In a group of its own, so that stopping it also stops the vite that npm started.
  const web = spawn('npm', ['exec', '-w', 'apps/web', '--', 'vite', '--port', '4721', '--strictPort'], { cwd: repo, stdio: 'ignore', detached: true, env: { ...process.env, ENGINE_URL: 'http://127.0.0.1:4720' } });
  const stop = () => {
    engine.kill();
    try { process.kill(-web.pid); } catch { web.kill(); }
    fs.rmSync(runner, { force: true }); fs.rmSync(work, { recursive: true, force: true });
  };
  try {
    let up = false;
    for (let i = 0; i < 150 && !up; i++) { try { up = (await fetch('http://127.0.0.1:4721/')).ok; } catch {} if (!up) await sleep(200); }
    if (!up) throw new Error('the Director dashboard did not start within 30 seconds');
    await sleep(5500);
    return await fn('http://127.0.0.1:4721/', cue);
  } finally { stop(); }
}
module.exports = { withDirector, sleep };

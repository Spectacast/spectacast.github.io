// Starts Spectacast Pass with the invented Demo Congress 2027 in one language, for the website's pictures.
//   await withPass(passRepo, 'de', async ({ base, info }) => { ... });
// info: { event, door, doorName, guest (the badge of a faculty member who has not arrived yet), snapshotAt }.
const { execFileSync, spawn } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const node = ['--disable-warning=ExperimentalWarning'];
const PORT = 4899;

async function withPass(repo, lang, fn) {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'pass-demo-'));
  const db = path.join(tmp, 'demo.db');
  const seed = path.join(__dirname, '..', 'screenshots', 'seed-pass.ts');
  const info = JSON.parse(execFileSync('node', [...node, seed, repo, db, lang]).toString());
  const hub = spawn('node', [...node, 'src/main.ts', '--db', db, '--port', String(PORT), '--https-port', '0'], { cwd: repo, stdio: 'ignore' });
  const base = `http://localhost:${PORT}`;
  try {
    for (let i = 0; i < 50; i++) { try { await fetch(base + '/api/events'); break; } catch { await new Promise((r) => setTimeout(r, 200)); } }
    return await fn({ base, info });
  } finally {
    hub.kill('SIGKILL');
    await new Promise((r) => (hub.exitCode !== null || hub.signalCode ? r() : hub.once('exit', r)));
    fs.rmSync(tmp, { recursive: true, force: true });
  }
}
module.exports = { withPass };

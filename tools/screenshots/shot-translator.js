// Screenshots of the Spectacast Translator control page for the website. The page is the real one
// from the Translator repository; its JSON API answers with an invented session (an Italian speaker
// translated into English), so no microphone or AI engine is needed.
//   node tools/screenshots/shot-translator.js <translator repo> <output folder>
const { chromium } = require('playwright');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');

const [repo, out] = process.argv.slice(2);
if (!repo || !out) throw new Error('usage: shot-translator.js <translator repo> <output folder>');
fs.mkdirSync(out, { recursive: true });
const web = path.join(repo, 'web');
const at = (s) => new Date(Date.UTC(2027, 2, 18, 9, 30, s)).toISOString();

const devices = { api: 'WASAPI', devices: [
  { id: 1, name: 'Hall A mixer (USB Audio CODEC)', inputChannels: 2, outputChannels: 2, isDefaultInput: true, isDefaultOutput: false, preferredRate: 48000 },
  { id: 2, name: 'Interpretation transmitter, channel 2', inputChannels: 0, outputChannels: 2, isDefaultInput: false, isDefaultOutput: true, preferredRate: 48000 },
  { id: 3, name: 'NDI: HALL-A (Program)', inputChannels: 2, outputChannels: 0, isDefaultInput: false, isDefaultOutput: false, preferredRate: 48000, ndi: 'HALL-A (Program)' },
] };
const request = { to: 'en', from: 'it', input: '1', output: '2', provider: 'gemini' };
const state = { running: true, wanted: true, connected: true, request,
  input: { id: 1, name: devices.devices[0].name, rate: 48000 }, output: { id: 2, name: devices.devices[1].name, rate: 48000 },
  providers: ['gemini', 'openai'] };
const lines = [
  ['input', 'Buongiorno a tutti e grazie per essere qui.'], ['output', 'Good morning everyone, and thank you for being here.'],
  ['input', 'Oggi vi mostro un caso in diretta dalla sala operatoria.'], ['output', 'Today I will show you a live case from the operating room.'],
  ['input', 'La paziente ha cinquantotto anni e nessun intervento precedente.'], ['output', 'The patient is fifty-eight years old, with no previous surgery.'],
  ['input', 'Iniziamo con tre accessi, come vedete sullo schermo.'], ['output', 'We start with three ports, as you can see on the screen.'],
  ['input', 'Se avete domande, scrivetele nella chat della riunione.'], ['output', 'If you have questions, write them in the meeting chat.'],
];
const events = [
  { type: 'log', at: at(0), level: 'info', message: 'Gemini session open: Italian → English' },
  { type: 'state', at: at(1), state },
  ...lines.map(([kind, text], i) => ({ type: 'transcript', at: at(4 + i * 3), kind, text })),
  { type: 'level', at: at(40), db: -18, open: true, heardMs: 312000, sentMs: 248000 },
];
const sse = events.map((e) => `event: ${e.type}\ndata: ${JSON.stringify(e)}\n\n`).join('') ;
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.json': 'application/json' };

// A small server in place of the Translator's own: the files of the page, the API, and an event
// stream that stays open (a closed one would show the page as disconnected).
const server = http.createServer((req, res) => {
  const p = new URL(req.url, 'http://x').pathname;
  const json = (body) => { res.writeHead(200, { 'content-type': 'application/json' }); res.end(JSON.stringify(body)); };
  if (p === '/api/events') { res.writeHead(200, { 'content-type': 'text/event-stream' }); res.write(sse); return; }
  if (p === '/api/devices') return json(devices);
  if (p === '/api/version') return json({ app: 'translator', version: '1.0.0', source: true });
  if (p.startsWith('/api/')) return json(state);
  const file = path.join(web, p === '/' ? 'index.html' : p);
  if (!file.startsWith(web) || !fs.existsSync(file) || !fs.statSync(file).isFile()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'content-type': types[path.extname(file)] || 'application/octet-stream' });
  res.end(fs.readFileSync(file));
});

(async () => {
  await new Promise((r) => server.listen(4730, '127.0.0.1', r));
  const b = await chromium.launch();
  for (const scheme of ['light', 'dark']) {
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, colorScheme: scheme, locale: 'en-GB', timezoneId: 'Europe/Berlin' });
    const pg = await ctx.newPage();
    await pg.goto('http://127.0.0.1:4730/'); await pg.waitForTimeout(2000);
    await pg.getByLabel('Topic').fill('Laparoscopic surgery, Dr. Chiara Fontana').catch(() => {});
    await pg.locator('body').click({ position: { x: 900, y: 700 } });
    await pg.screenshot({ path: `${out}/translator-${scheme}.png` });
    await ctx.close();
  }
  await b.close();
  server.closeAllConnections(); server.close();
  console.log('Translator screenshots in', out);
})().catch((e) => { console.error(e); process.exit(1); });

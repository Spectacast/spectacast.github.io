// Fills a Pass database with the invented "Demo Congress 2027", for the website's screenshots.
// No real person or event appears: names are drawn from the lists below with a fixed seed.
//   node tools/screenshots/seed-pass.ts <pass repo> <database file>
// The day is today, 08:30 to 18:00 in Berlin, with scans until 15:30: take the screenshots with the
// browser clock set to SNAPSHOT_AT (shot.ts does), so it looks the same whenever it is run.
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const [passRepo, dbFile] = process.argv.slice(2);
if (!passRepo || !dbFile) throw new Error('usage: seed-pass.ts <pass repo> <database file>');
const { Store } = await import(pathToFileURL(path.resolve(passRepo, 'src/store.ts')).href);

let seed = 20271;
const rand = () => ((seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648);
const pick = <T>(xs: T[]): T => xs[Math.floor(rand() * xs.length)]!;

const FIRST = ['Anna', 'Luca', 'Sofia', 'Jonas', 'Marta', 'Pablo', 'Elena', 'Tobias', 'Giulia', 'Mateo',
  'Clara', 'Nils', 'Irene', 'Hugo', 'Lea', 'Diego', 'Chiara', 'Felix', 'Nora', 'Andrés', 'Paula', 'Marco',
  'Hanna', 'Javier', 'Alice', 'Emil', 'Carmen', 'Davide', 'Lena', 'Ruben', 'Ines', 'Matteo', 'Greta',
  'Álvaro', 'Sara', 'Leon', 'Beatriz', 'Pietro', 'Mia', 'Óscar'];
const LAST = ['Weber', 'Rossi', 'García', 'Becker', 'Conti', 'Navarro', 'Hoffmann', 'Greco', 'Ortega',
  'Krüger', 'Marini', 'Delgado', 'Vogel', 'Ferri', 'Romero', 'Lange', 'Gallo', 'Castillo', 'Brandt',
  'Moretti', 'Serrano', 'Keller', 'Fontana', 'Molina', 'Hartmann', 'Barbieri', 'Iglesias', 'Busch',
  'Herrera', 'Seidel', 'Caruso', 'Vidal', 'Winter', 'Rinaldi', 'Pascual'];

const store = new Store(dbFile, { name: 'Demo Events' });
const hour = 3600_000;
const day = new Date().toISOString().slice(0, 10);
// Berlin's offset from UTC today, e.g. "GMT+1".
const off = new Intl.DateTimeFormat('en', { timeZone: 'Europe/Berlin', timeZoneName: 'shortOffset' })
  .formatToParts(new Date(`${day}T12:00:00Z`)).find((p) => p.type === 'timeZoneName')!.value;
const offHours = Number(off.replace('GMT', '') || 0);
const start = new Date(Date.parse(`${day}T08:30:00Z`) - offHours * hour); // 08:30 in Berlin
const at = (h: number) => new Date(start.getTime() + h * hour).toISOString();
export const SNAPSHOT_AT = new Date(start.getTime() + 7 * hour + 60_000); // 15:31 in Berlin

const event = store.createEvent({
  name: 'Demo Congress 2027', timeZone: 'Europe/Berlin', startsOn: day, endsOn: day,
  settings: { dayEnd: '23:59', doubleReadSeconds: 5, language: 'en', highlightBelowPercent: 60 },
});
const id = event.id;

const cats = [
  ['Delegate', '#4a6fa5', 'DELEGATE', 150], ['Faculty', '#7a4e9b', 'FACULTY', 30],
  ['Industry', '#2c6e64', 'INDUSTRY', 25], ['Press', '#8a6d3b', 'PRESS', 8], ['Staff', '#55606e', 'STAFF', 12],
].map(([name, color, label, n]) => ({ cat: store.create('categories', id, { name, color, label }), n: n as number }));

const zones = [
  ['Hall A', 'hall', 400], ['Hall B', 'hall', 220], ['Workshop room', 'room', 40], ['Exhibition', 'exhibition', null],
].map(([name, kind, capacity]) => store.create('zones', id, { name, kind, capacity }));
const doors = zones.map((z) => store.create('doors', id, { zoneId: z.id, name: `${z.name} door`, direction: 'both' }));

const titles = [
  ['Opening and keynote', 'Live case: minimally invasive surgery', 'Panel: training the next generation',
    'Live case: complex reconstruction', 'Best papers and closing'],
  ['Imaging today', 'Robotics in practice', 'Lunch symposium', 'Complications and how to avoid them', 'Video session'],
  ['Hands-on: suturing', 'Hands-on: energy devices', 'Hands-on: simulators', 'Hands-on: stapling', 'Hands-on: review'],
];
const sessions = titles.map((list, zi) =>
  list.map((title, i) => store.create('sessions', id, {
    zoneId: zones[zi]!.id, title, startsAt: at(0.5 + i * 1.75), endsAt: at(2 + i * 1.75), counts: zi < 2,
  })),
);

const used = new Set<string>();
const people: { code: string; cat: string }[] = [];
for (const { cat, n } of cats)
  for (let i = 0; i < n; i++) {
    let first: string, last: string;
    do { first = pick(FIRST); last = pick(LAST); } while (used.has(first + last) && used.size < FIRST.length * LAST.length);
    used.add(first + last);
    const { badge } = store.addAttendee(id, {
      firstName: first, lastName: last,
      email: `${first}.${last}`.toLowerCase().normalize('NFD').replace(/[^\x00-\x7f]/g, '') + '@example.org',
      categoryId: cat.id, status: 'active', tags: [], fields: {}, source: 'demo', sourceId: `${people.length + 1}`,
    });
    people.push({ code: badge.code, cat: cat.name });
  }

// One faculty member who has not arrived yet: shot.ts scans her badge at the Hall A door.
const faculty = cats.find((c) => c.cat.name === 'Faculty')!.cat;
const guest = store.addAttendee(id, {
  firstName: 'Sofia', lastName: 'Navarro', email: 'sofia.navarro@example.org', categoryId: faculty.id,
  status: 'active', tags: [], fields: {}, source: 'demo', sourceId: 'guest',
}).badge.code;

// The day so far: most people come to Hall A first, move between rooms, a few leave early; about two
// thirds are still inside now.
const now = SNAPSHOT_AT.getTime();
const scan = (code: string, door: { id: string }, t: number) => {
  if (t >= now - 60_000) return;
  store.decideAndRecord(id, { code, doorId: door.id, at: new Date(t).toISOString(), mode: 'auto' });
};
for (const p of people) {
  let t = start.getTime() + (0.1 + rand() * 0.9) * hour;
  let zone = rand() < 0.7 ? 0 : 1;
  if (p.cat === 'Industry') zone = 3;
  while (t < now) {
    scan(p.code, doors[zone]!, t);
    const stay = (0.6 + rand() * 2.2) * hour;
    if (t + stay >= now) break;
    scan(p.code, doors[zone]!, t + stay); // out
    t += stay + (0.1 + rand() * 0.4) * hour;
    if (rand() < 0.08) break; // gone home
    zone = p.cat === 'Industry' ? 3 : pick([0, 0, 0, 1, 1, 2, 3]);
  }
}
console.log(JSON.stringify({ event: id, attendees: people.length, scans: store.scans(id).length,
  snapshotAt: SNAPSHOT_AT.toISOString(), guest, door: doors[0]!.id }));
store.close();

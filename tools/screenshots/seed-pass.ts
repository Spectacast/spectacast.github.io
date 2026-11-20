// Fills a Pass database with the invented "Demo Congress 2027", for the website's screenshots.
// No real person or event appears: names are drawn from the lists below with a fixed seed.
//   node tools/screenshots/seed-pass.ts <pass repo> <database file> [en|de|es|it]
// In another language the event speaks it too: its rooms, doors, categories, sessions and door messages.
// The day is today, 08:30 to 18:00 in Berlin, with scans until 15:30: take the screenshots with the
// browser clock set to SNAPSHOT_AT (shot.ts does), so it looks the same whenever it is run.
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const [passRepo, dbFile, lang = 'en'] = process.argv.slice(2);
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

// What the organiser would have typed, in each language.
const NAMES = {
  en: {
    zones: ['Hall A', 'Hall B', 'Workshop room', 'Exhibition'], door: (z: string) => `${z} door`,
    cats: [['Delegate', 'DELEGATE'], ['Faculty', 'FACULTY'], ['Industry', 'INDUSTRY'], ['Press', 'PRESS'], ['Staff', 'STAFF']],
    titles: [
      ['Opening and keynote', 'Live case: minimally invasive surgery', 'Panel: training the next generation',
        'Live case: complex reconstruction', 'Best papers and closing'],
      ['Imaging today', 'Robotics in practice', 'Lunch symposium', 'Complications and how to avoid them', 'Video session'],
      ['Hands-on: suturing', 'Hands-on: energy devices', 'Hands-on: simulators', 'Hands-on: stapling', 'Hands-on: review'],
    ],
  },
  de: {
    zones: ['Saal A', 'Saal B', 'Workshop-Raum', 'Ausstellung'], door: (z: string) => `Eingang ${z}`,
    cats: [['Teilnehmende', 'TEILNEHMENDE'], ['Referierende', 'FACULTY'], ['Industrie', 'INDUSTRIE'], ['Presse', 'PRESSE'], ['Team', 'TEAM']],
    titles: [
      ['Eröffnung und Keynote', 'Live-OP: minimalinvasive Chirurgie', 'Podium: die nächste Generation ausbilden',
        'Live-OP: komplexe Rekonstruktion', 'Beste Beiträge und Abschluss'],
      ['Bildgebung heute', 'Robotik in der Praxis', 'Lunch-Symposium', 'Komplikationen und wie man sie vermeidet', 'Videositzung'],
      ['Hands-on: Nahttechnik', 'Hands-on: Energiegeräte', 'Hands-on: Simulatoren', 'Hands-on: Klammernaht', 'Hands-on: Rückblick'],
    ],
  },
  es: {
    zones: ['Sala A', 'Sala B', 'Sala de talleres', 'Exposición'], door: (z: string) => `Puerta ${z}`,
    cats: [['Congresista', 'CONGRESISTA'], ['Ponente', 'PONENTE'], ['Industria', 'INDUSTRIA'], ['Prensa', 'PRENSA'], ['Organización', 'ORGANIZACIÓN']],
    titles: [
      ['Inauguración y conferencia magistral', 'Cirugía en directo: mínimamente invasiva', 'Mesa redonda: formar a la próxima generación',
        'Cirugía en directo: reconstrucción compleja', 'Mejores comunicaciones y clausura'],
      ['La imagen hoy', 'Robótica en la práctica', 'Simposio del almuerzo', 'Complicaciones y cómo evitarlas', 'Sesión de vídeos'],
      ['Taller: sutura', 'Taller: dispositivos de energía', 'Taller: simuladores', 'Taller: grapado', 'Taller: repaso'],
    ],
  },
  it: {
    zones: ['Sala A', 'Sala B', 'Sala workshop', 'Esposizione'], door: (z: string) => `Ingresso ${z}`,
    cats: [['Partecipante', 'PARTECIPANTE'], ['Faculty', 'FACULTY'], ['Aziende', 'AZIENDE'], ['Stampa', 'STAMPA'], ['Staff', 'STAFF']],
    titles: [
      ['Apertura e lettura magistrale', 'Chirurgia in diretta: mininvasiva', 'Tavola rotonda: formare la prossima generazione',
        'Chirurgia in diretta: ricostruzione complessa', 'Migliori contributi e chiusura'],
      ['Imaging oggi', 'Robotica nella pratica', 'Simposio del pranzo', 'Complicanze e come evitarle', 'Sessione video'],
      ['Hands-on: sutura', 'Hands-on: dispositivi a energia', 'Hands-on: simulatori', 'Hands-on: suturatrici', 'Hands-on: ripasso'],
    ],
  },
}[lang as 'en' | 'de' | 'es' | 'it'];
if (!NAMES) throw new Error(`no demo names in "${lang}"`);

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
  settings: { dayEnd: '23:59', doubleReadSeconds: 5, language: lang, highlightBelowPercent: 60 },
});
const id = event.id;

// Delegates, faculty, industry, press, staff: in this order, whatever they are called.
const FACULTY = 1, INDUSTRY = 2;
const cats = ([['#4a6fa5', 150], ['#7a4e9b', 30], ['#2c6e64', 25], ['#8a6d3b', 8], ['#55606e', 12]] as [string, number][])
  .map(([color, n], i) => ({ cat: store.create('categories', id, { name: NAMES.cats[i]![0], color, label: NAMES.cats[i]![1] }), n, kind: i }));

const zones = ([['hall', 400], ['hall', 220], ['room', 40], ['exhibition', null]] as [string, number | null][])
  .map(([kind, capacity], i) => store.create('zones', id, { name: NAMES.zones[i], kind, capacity }));
const doors = zones.map((z) => store.create('doors', id, { zoneId: z.id, name: NAMES.door(z.name), direction: 'both' }));

const titles = NAMES.titles;
const sessions = titles.map((list, zi) =>
  list.map((title, i) => store.create('sessions', id, {
    zoneId: zones[zi]!.id, title, startsAt: at(0.5 + i * 1.75), endsAt: at(2 + i * 1.75), counts: zi < 2,
  })),
);

const used = new Set<string>();
const people: { code: string; kind: number }[] = [];
for (const { cat, n, kind } of cats)
  for (let i = 0; i < n; i++) {
    let first: string, last: string;
    do { first = pick(FIRST); last = pick(LAST); } while (used.has(first + last) && used.size < FIRST.length * LAST.length);
    used.add(first + last);
    const { badge } = store.addAttendee(id, {
      firstName: first, lastName: last,
      email: `${first}.${last}`.toLowerCase().normalize('NFD').replace(/[^\x00-\x7f]/g, '') + '@example.org',
      categoryId: cat.id, status: 'active', tags: [], fields: {}, source: 'demo', sourceId: `${people.length + 1}`,
    });
    people.push({ code: badge.code, kind });
  }

// One faculty member who has not arrived yet: shot.ts scans her badge at the Hall A door.
const faculty = cats[FACULTY]!.cat;
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
  if (p.kind === INDUSTRY) zone = 3;
  while (t < now) {
    scan(p.code, doors[zone]!, t);
    const stay = (0.6 + rand() * 2.2) * hour;
    if (t + stay >= now) break;
    scan(p.code, doors[zone]!, t + stay); // out
    t += stay + (0.1 + rand() * 0.4) * hour;
    if (rand() < 0.08) break; // gone home
    zone = p.kind === INDUSTRY ? 3 : pick([0, 0, 0, 1, 1, 2, 3]);
  }
}
console.log(JSON.stringify({ event: id, attendees: people.length, scans: store.scans(id).length,
  snapshotAt: SNAPSHOT_AT.toISOString(), guest, door: doors[0]!.id, doorName: doors[0]!.name, label: NAMES.cats[FACULTY]![1] }));
store.close();

# Regeln und Skripte

<p class="lede">Eine Regel tut, was sonst ein Operator von Hand täte: Wenn etwas geschieht und eine Bedingung zutrifft, führt sie eine Liste von Schritten aus. Dank der Regeln kann ein einziger Operator viele Säle im Blick behalten.</p>

## Eine Regel hat drei Teile

1. **Auslöser:** ein Ereignis eines Geräts (jemand betritt den Warteraum), ein Wert im Zustand, der sich ändert (ein OBS beginnt zu streamen), ein Intervall oder **manuell starten**. Ein Auslöser kann ein Gerät beobachten oder jedes Gerät eines Treibers, sodass eine Regel für alle Säle reicht.
2. **Bedingung** (optional): ein Ausdruck, der zutreffen muss, etwa `obs.studioA.streaming`.
3. **Schritte:** dieselben Schritte, die eine Taste ausführt. Siehe [Panels](/de/hilfe/director-panels/).

Auf der Seite **Regeln** legt **+ Regel** eine leere Regel an, und **+ aus Vorlage** baut eine gängige Regel aus Ihren eigenen Geräten, zum Beispiel „die sprechende Person geht nach einer Haltezeit auf eine Szene“ oder „eine NDI-Quelle fällt aus, auf eine Ersatzszene wechseln“.

{{shot:director-rules|Die Regeln in Director: jede mit ihrem Auslöser und dem letzten Lauf}}

## Zeit und Reihenfolge

- **Haltezeit (ms):** Die Regel wartet, und nur der letzte Auslöser einer Folge zählt. Wer spricht, muss das Wort einen Moment behalten, bevor das Bild wechselt.
- **Sperrzeit (ms):** So lange läuft die Regel nicht noch einmal.
- **Priorität:** Wenn ein Ereignis zu mehreren Regeln passt, läuft die höhere zuerst.

## Erst testen, dann vertrauen

- **Probelauf:** Die Regel protokolliert, was sie täte, und tut nichts.
- **Jetzt ausführen** führt eine Regel einmal aus, unabhängig von ihrem Auslöser.
- **Verlauf**, unten auf der Seite, listet jeden Lauf und jedes Auslassen mit dem Grund auf, und jede Aktion mit ihrem Fehler.
- **Diagramm** zeichnet alle Regeln: links die Auslöser, in der Mitte die Regeln, rechts die Geräte, auf die sie wirken.

Der Schalter **AUTOMATIK AN** in der Kopfzeile pausiert alle Regeln auf einmal und zeigt **AUTOMATIK AUS**, solange sie pausiert sind. Die Tasten funktionieren weiter.

## Skript-Schritte

Für Logik, die die Formulare nicht ausdrücken können, kann ein Schritt ein kurzes Stück JavaScript sein. Es läuft auf dem Regie-PC und hat alles Nötige zur Hand:

| Name | Was es ist |
|---|---|
| `state` | Alles, was Director über jedes Gerät weiß |
| `event` | Was die Regel ausgelöst hat |
| `vars` | Die Variablen |
| `setVar(id, value)` | Setzt eine Variable |
| `await run(target, action, params)` | Führt eine Aktion auf einem Gerät aus |
| `log(...)` | Schreibt eine Zeile ins Ereignisprotokoll |
| `await sleep(ms)` | Wartet |

```
// Auslöser: das Ereignis "Entered the waiting room" eines Meetings.
// Die Referenten sofort einlassen; alle anderen warten auf den Operator.
if (event.name.startsWith('Dr.')) {
  await run({ eventDevice: true }, 'admit', { by: 'zoomID', user: event.zoomId });
  log('admitted', event.name);
}
```

**Testen (Probelauf)** im Editor führt das Skript einmal aus, ohne ein Gerät anzufassen, und zeigt sein Protokoll. Ein Skript, das fehlschlägt oder länger als fünf Sekunden läuft, zählt als ein fehlgeschlagener Schritt, und die Schritte danach laufen trotzdem.

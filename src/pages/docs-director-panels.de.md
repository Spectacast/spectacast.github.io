# Panels

<p class="lede">Ein Panel ist eine Seite mit Bedienelementen, die Sie selbst anordnen: Tasten, Schalter, Auswahlen, Textfelder und die Kacheln jedes Saals. Die Panels der Beispiel-Show sind ein Ausgangspunkt, und jedes lässt sich ändern.</p>

{{shot:director-panels|Ein Panel in Director mit vier Sälen: ein Block pro Saal, mit Meeting, Warteraum, Preview und Program}}

## Ein Panel bearbeiten

Klicken Sie auf der Seite **Panels** auf **Bearbeiten**. Jetzt fügt ein Klick auf eine leere Zelle ein Bedienelement hinzu, und ein Klick auf ein Bedienelement öffnet seine Eigenschaften.

- Wählen Sie mehrere Bedienelemente mit Umschalt-Klick oder durch Aufziehen eines Rechtecks aus und verschieben, kopieren oder löschen Sie sie gemeinsam.
- **Rückgängig** und **Wiederholen** gehen bis zu hundert Schritte zurück und vor.
- **Speichern** übernimmt die Änderungen für jedes Dashboard; **Verwerfen** verwirft sie.

**+ Panel** fügt eine Seite hinzu. Wer sich mit der Operator-PIN anmeldet, sieht die Panels und sonst nichts.

## Bedienelemente

| Bedienelement | Was es tut |
|---|---|
| **Taste** | Führt beim Drücken ihre Schritte aus |
| **Schalter** | Eine Liste von Schritten zum Einschalten, eine zum Ausschalten |
| **Auswahl (Optionen)** | Eine Reihe von Optionen: eine feste Liste oder eine aktuelle, etwa die Szenen eines OBS oder die Personen in einem Meeting |
| **Text** | Ein Feld mit einer Taste zum Übernehmen, für eine Bauchbinde oder einen Namen |
| **Beschriftung** | Zeigt einen Text oder einen Wert |
| **Gerätestatus** | Zeigt, ob ein Gerät verbunden ist |
| **Vorschau (Bild eines Geräts)** | Das Live-Bild eines OBS oder einer NDI-Quelle |
| **Mixer (Audioeingänge eines Geräts)** | Fader und Stummschaltung für die Audioeingänge eines Geräts |
| **Rahmen (Gruppe)** | Ein Rahmen mit Titel um Bedienelemente, die zusammengehören |
| **Block** | Eine Gruppe von Bedienelementen, einmal gebaut und viele Male platziert |

## Was ein Tastendruck tut

Ein Tastendruck führt eine Liste von Schritten aus, von oben nach unten:

- eine **Aktion** auf einem Gerät, etwa „Programmszene wechseln“;
- eine **Wartezeit**;
- das **Setzen einer Variablen**;
- ein **Wenn** mit einer Liste für Ja und einer für Nein;
- Schritte, die **parallel** laufen oder einmal **für jedes** Element einer Liste.

**Vorher fragen** lässt das Dashboard eine Frage stellen, bevor es die Schritte ausführt: für die Tasten, die niemand versehentlich drücken soll.

## Rückmeldung: wie ein Bedienelement aussieht

Einträge unter **Rückmeldung** ändern Farbe und Text eines Bedienelements nach dem aktuellen Zustand: rot, solange ein Saal auf Sendung ist, ein Name, wenn jemand im Warteraum ist. Die Einträge werden von oben geprüft, und der erste, der zutrifft, gilt.

## Blöcke: ein Kanalstreifen für jeden Saal

Bauen Sie die Bedienelemente eines Saals einmal, wählen Sie sie aus und klicken Sie auf **Block erstellen**. Die Geräte, die sie nennen, werden zu den **Werten** des Blocks. Platzieren Sie den Block einmal pro Saal und geben Sie jeder Platzierung ihre eigenen Geräte. Eine Änderung am Block erreicht jeden Saal zugleich.

## Variablen

Die Seite **Variablen** enthält Werte, die Panels und Regeln gemeinsam nutzen: den gewählten Clip, die Person, die gerade das Wort hat. **Variable hinzufügen** legt eine an, mit ihrem Typ und ihrem Anfangswert.

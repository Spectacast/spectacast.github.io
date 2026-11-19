# Geräte und Treiber

<p class="lede">Alles, was Director steuert, ist ein Gerät: das OBS eines Saals, sein Meeting, ein Empfänger für Telefon-Mikrofone, ein Funkempfänger, ein MIDI-Controller. Ein Treiber sagt Director, was eine Geräteart kann und was sie meldet.</p>

## Ein Gerät hinzufügen

1. Öffnen Sie die Seite **Geräte** und gehen Sie zum Formular **Gerät hinzufügen** unter den Karten.
2. Wählen Sie den Treiber und geben Sie einen Namen ein. Das Formular zeigt für jede Einstellung, die der Treiber braucht, ein Feld mit seinem Standardwert.
3. Klicken Sie auf **Hinzufügen**. Der Punkt auf der Karte wird grün, sobald das Gerät antwortet; die Karte zeigt seinen Zustand und den letzten Fehler.

**bearbeiten** auf einer Karte ändert den Namen und die Einstellungen; Director verbindet sich beim Speichern neu. **Netzwerk durchsuchen** und dann **suchen** listet jedes OBS und jedes Spectacast Meet auf, das im Netzwerk antwortet; **im Formular verwenden** füllt das Formular mit einem davon.

Das OBS-Passwort steht nicht in der Show-Datei: Tragen Sie es in `C:\ProgramData\Spectacast\director\.env` als `OBS_PASSWORD=<Passwort>` ein und melden Sie sich dann ab und wieder an. Das Passwort eines Sennheiser-Empfängers oder eines Mic-Empfängers wird in der Show-Datei gespeichert.

## Die Treiber, die Director mitbringt

| Treiber | Was Director sieht und tut |
|---|---|
| **OBS Studio** | Szenen, Quellen, Ton, Aufnahme und Streaming eines OBS, über dessen WebSocket-Server |
| **NDI discovery** | Die NDI-Quellen im Netzwerk, auch über einen NDI Discovery Server. Ein Bedienelement **Vorschau** zeigt das Bild jeder dieser Quellen |
| **Spectacast Meet** | Wer im Meeting und im Warteraum ist; einlassen, stummschalten und ins Spotlight setzen; welches Signal an welchen Ausgang geht |
| **Spectacast Mic** | Die Telefone, die als Mikrofone und Kommando mit einem Saal-PC verbunden sind |
| **Translator** | Eine Übersetzung starten und stoppen, die Sprachen wählen, lesen, was gehört und was gesagt wurde |
| **Sennheiser EW-DX receiver** | Stummschaltung, Gain, Pegel, Funkverbindung und Batterie jedes Kanals. Schalten Sie zuerst in Sennheiser Control Cockpit den 3rd Party Access ein (Firmware 4.0.0 oder neuer) |
| **MIDI controller** | Noten und Controller in beide Richtungen: Fader und Tasten eines Bedienpults |
| **Folder of files** | Die Clips in einem Ordner, lokal oder freigegeben; eine hineinkopierte Datei erscheint von selbst |
| **Recorder** | Zeichnet das Meeting-Signal eines Saals in stündlichen Dateien auf |

Ein Gerät, das nicht auf dieser Liste steht, bekommt auf der Seite **Treiber** einen eigenen Treiber, ohne Code: siehe [Ihr eigener Treiber](/de/hilfe/director-drivers/).

## Eingänge von außen

Über zwei Eingänge kann ein anderes System in Director etwas auslösen. Beide stehen auf der Seite **Geräte** unter **Eingänge**.

- **Webhooks:** Ein Aufruf von `POST /api/hooks/<name>` löst das Ereignis `<name>` aus. Der JSON-Body und die Parameter der Adresse kommen als Felder des Ereignisses an.
- **OSC-Eingang:** Legen Sie einen Port fest, und jede OSC-Nachricht, die dort ankommt, wird zu einem Ereignis mit dem Namen ihrer Adresse: Aus `/cue/go` wird `cue_go`.

Eine Regel reagiert dann auf das Ereignis. Siehe [Regeln und Skripte](/de/hilfe/director-rules/) und [API, Webhooks und Stream Deck](/de/hilfe/director-api/).

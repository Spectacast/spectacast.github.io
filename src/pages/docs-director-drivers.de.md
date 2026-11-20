# Ihr eigener Treiber

<p class="lede">Die Seite Treiber beschreibt das Protokoll eines Geräts ohne Code. Danach hat das Gerät Aktionen, Ereignisse und einen Zustand wie ein mitgeliefertes, und Panels und Regeln nutzen es genauso.</p>

Ein selbst definierter Treiber spricht einen von fünf Transporten: **OSC**, **UDP**, **TCP**, **HTTP** oder **WebSocket**. Das deckt die meisten Lichtpulte, Audiomischer, Bildmischer, Kreuzschienen und Haussteuerungen ab.

## 1. Den Treiber anlegen

Klicken Sie auf der Seite **Treiber** auf **+ Treiber über…** und wählen Sie den Transport. Geben Sie dem Treiber einen Namen und listen Sie die Einstellungen auf, die jedes seiner Geräte braucht: einen Host, einen Port, einen API-Schlüssel. Eine Einstellung hat einen Standardwert oder ist mit **Pfl.** (Pflichtfeld) markiert, und die Vorlagen unten lesen sie als `config.<id>`.

{{closeup:director-build-driver|Nahaufnahme des Treiber-Editors von Director mit dem Beispiel „Generic OSC device“: der Transport OSC über UDP, die Einstellungen, die jedes Gerät verlangt, und die ersten Befehle|**Wie es spricht**: OSC, UDP, TCP, HTTP oder WebSocket.|**Was jedes Gerät braucht**: hier zwei Ports, neben seiner Adresse.|**Seine Befehle**: Jeder wird zu einer Aktion für Tasten und Regeln.}}

## 2. Befehle

Klicken Sie für alles, was man dem Gerät sagen kann, auf **+ Befehl**. Ein Befehl wird zu einer Aktion, die Tasten und Regeln ausführen können.

- Seine **Parameter** sind typisierte Felder, die in der Nachricht als `params.<id>` gelesen werden.
- Seine **Nachricht** ist eine Vorlage. Bei OSC ist sie eine Adresse mit typisierten Argumenten, etwa `/cue/{{params.cue}}/go`. Bei HTTP ist sie eine Methode, ein Pfad, Header und ein Body. Bei UDP, TCP und WebSocket ist sie eine Textzeile, oder für ein binäres Protokoll Bytes in Hex-Schreibweise.

## 3. Rückmeldung

Klicken Sie für jede Nachricht, die das Gerät zurückschickt, auf **+ Rückmeldungseintrag**. Ein Eintrag erkennt eine Nachricht und legt fest, was mit ihr geschieht.

- **Erkennen** über ein OSC-Adressmuster (`/cue/{n}/active`, wobei `{n}` einen Teil der Adresse aufnimmt), über einen regulären Ausdruck auf Text oder über einen Ausdruck auf eine JSON-Nachricht.
- **Zustand setzen:** Werte aus der Nachricht in den Zustand des Geräts schreiben, wo Panels sie anzeigen und Regeln sie lesen.
- **Ein Ereignis auslösen**, auf das eine Regel reagieren kann.

Ein HTTP-Treiber kann außerdem **abfragen**: Er ruft alle paar Sekunden eine Adresse auf und schickt die Antwort durch dieselben Einträge.

## 4. Online oder offline

TCP- und WebSocket-Geräte sind online, solange die Verbindung steht, und Director verbindet sich von selbst neu. UDP-, OSC- und HTTP-Geräte brauchen einen **Heartbeat**: einen Befehl, der in einem festen Abstand gesendet wird und dessen Antwort zeigt, dass das Gerät da ist. Ohne ihn gelten sie als online.

## 5. Am echten Gerät ausprobieren

Klicken Sie auf **Treiber anlegen** und fügen Sie dann auf der Seite **Geräte** ein Gerät mit Ihrem Treiber hinzu. Zurück auf der Seite **Treiber** klicken Sie auf der Karte des Treibers auf **testen**, wählen das Gerät und klicken auf **Nachrichten mitschneiden**. Jede ein- und ausgehende Nachricht wird live aufgelistet, und jede eingehende zeigt, welche Rückmeldungseinträge auf sie passen und was sie setzen würden. **Test senden** führt einen Befehl mit den Parametern aus, die Sie eingeben.

## 6. Weitergeben

**exportieren** lädt die Definition als JSON-Datei herunter; **JSON importieren** fügt eine in eine andere Show ein. Die Definitionen werden in der Show-Datei gespeichert, eine Show bringt ihre Treiber also mit.

Zwei Beispiele zum Importieren und Anpassen: [ein allgemeines OSC-Gerät](/examples/drivers/generic-osc.json) und [ein HTTP-Gerät, dessen Status abgefragt wird](/examples/drivers/http-example.json).

## Wenn das nicht reicht

Ein Gerät, das die eigene Bibliothek seines Herstellers braucht, oder ein Protokoll, das diese fünf Transporte nicht tragen, braucht einen in Director eingebauten Treiber. [Schreiben Sie uns](/de/kontakt/), welches Gerät Sie steuern möchten.

# Zum Erweitern gebaut

<p class="lede">An jedem Veranstaltungsort steht ein Gerät, mit dem niemand gerechnet hat. Spectacast Director ist so gemacht, dass Sie es selbst anbinden können: sein Protokoll in einem Formular beschreiben, per Skript ergänzen, was die Formulare nicht sagen können, und alles über seine API aus Ihren eigenen Systemen steuern.</p>

{{cta}}

## Ein Gerät ohne Code anbinden

Auf der Seite Treiber beschreiben Sie das Protokoll eines Geräts: die Befehle, die es annimmt, und die Nachrichten, die es zurückschickt. Director spricht OSC, UDP, TCP, HTTP und WebSocket; das deckt die meisten Lichtpulte, Audiomischer, Bildmischer und Kreuzschienen ab. Danach hat das Gerät Tasten, einen Live-Zustand und Regeln wie die mitgelieferten.

Sie testen am echten Gerät, wobei jede ein- und ausgehende Nachricht live aufgelistet wird, und geben einen fertigen Treiber als eine Datei weiter.

[So beschreiben Sie einen Treiber →](/de/hilfe/director-drivers/)

{{closeup:director-build-driver|Nahaufnahme des Treiber-Editors von Director mit dem Beispiel „Generic OSC device“: der Transport OSC über UDP, die Einstellungen, die jedes Gerät verlangt, und die ersten Befehle|**Wie es spricht**: OSC, UDP, TCP, HTTP oder WebSocket.|**Was jedes Gerät braucht**: hier zwei Ports, neben seiner Adresse.|**Seine Befehle**: Jeder wird zu einer Aktion für Tasten und Regeln.}}

## Regeln, und Skripte, wenn Regeln nicht reichen

Regeln reagieren auf das, was in den Sälen geschieht: Jemand betritt den Warteraum, eine Person ergreift das Wort, eine Quelle fällt aus. Die meisten entstehen aus Formularen. Wo die Logik Ihre eigene ist, kann ein Schritt aus ein paar Zeilen JavaScript bestehen, mit dem ganzen Zustand zur Hand.

{{closeup:director-build-rule|Nahaufnahme des Regel-Editors von Director mit der Regel „Active speaker → Speaker“: Wenn in Zoom Saal A die sprechende Person wechselt, setzt OBS Saal A nach einer Haltezeit von 1500 ms seine Szene|**Wenn**: was die Regel auslöst. Hier wechselt in Saal A die sprechende Person.|**Nur wenn**: eine Bedingung und eine Haltezeit. Hier muss die Person das Wort anderthalb Sekunden behalten.|**Dann**: was die Regel tut. Hier wechselt OBS in Saal A die Szene.}}

[Regeln und Skripte →](/de/hilfe/director-rules/)

## Eine API für Ihre eigenen Systeme

Alles, was das Dashboard tut, läuft über eine HTTP-API auf dem Regie-PC, und ein WebSocket sendet jede Änderung, sobald sie geschieht. Ein Registrierungssystem, eine Showsteuerung oder ein Skript kann den Zustand jedes Saals lesen, eine Taste drücken, eine Variable setzen oder eine Regel ausführen, jeweils mit einem Token, das begrenzt, was es darf.

[Die API →](/de/hilfe/director-api/)

## Webhooks und OSC-Eingang

Ein anderes System löst in Director mit einem einzigen Aufruf etwas aus: mit einem Webhook über HTTP oder mit einer OSC-Nachricht. Das Programm des Kongresses kann eine Sitzung ankündigen, und eine Regel setzt den richtigen Titel auf den richtigen Saal.

## Stream Deck und MIDI

Eine Taste des Stream Deck drückt über Bitfocus Companion jedes Bedienelement des Dashboards, ohne zusätzliche Installation. Ein MIDI-Bedienpult gibt dem Operator echte Fader und Tasten, und Regeln können sie leuchten lassen.

## Ihre eigenen Panels

Die Panels des Dashboards ordnen Sie selbst an: Tasten, Auswahlen, Textfelder, Pegelanzeigen und Live-Bilder, einmal als Block gebaut und einmal pro Saal platziert.

{{closeup:director-build-panel|Nahaufnahme des Panel-Editors von Director: die Reihe der fertigen Blöcke, das Raster des Panels mit leeren Zellen und die Taste Speichern|**Blöcke**: ein ganzer Saal, ein Meeting oder ein Monitor, einmal gebaut und überall eingesetzt.|**Auf eine leere Zelle klicken**, um ein Bedienelement hinzuzufügen oder einen Block einzusetzen, oder auf ein Bedienelement, um es zu ändern.|**Speichern**, und das Panel ist einsatzbereit.}}

[Panels →](/de/hilfe/director-panels/)

## Ihr Gerät lässt sich so nicht anbinden?

Manche Geräte brauchen die eigene Bibliothek ihres Herstellers. Diese Treiber sind in Director eingebaut, wie die für OBS Studio, NDI und Sennheiser EW-DX.

[Schreiben Sie uns, was Sie steuern möchten →](/de/kontakt/)

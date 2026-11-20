# Spectacast Director

<p class="lede">Die Regie für hybride Live-Veranstaltungen. Ein Dashboard sieht alle Saal-PCs, das Online-Meeting und die Mikrofone zugleich, und Regeln übernehmen, was sonst jemand in der Regie viele Male am Tag von Hand erledigt.</p>

{{cta}}

{{loop:director-speaker|Referentin auswählen, Mikrofon öffnen, ins Spotlight setzen. Drei Berührungen.|Bildschirmaufnahme von Director: Der Operator wählt Dr. Elena Ortega in Saal A, öffnet ihr Mikrofon und setzt sie ins Spotlight}}

## Jeder Saal auf einem Bildschirm

Jeder Saal hat seinen eigenen Streifen: wer im Meeting ist und wer spricht, Warteraum und Lobby, Preview und Program, Banner und Stream. Sie wählen eine Rednerin, bringen sie mit einem Tippen auf Sendung, und der nächste Saal steht gleich daneben. Eine Person kann einen ganzen Kongress verfolgen; beim Kongress mit 18 Sälen, für den Director gebaut wurde, war es genau eine.

{{closeup:director-hall|Nahaufnahme von Saal A und Saal B in Director: beide auf Sendung, je vier Personen im Meeting mit Mikrofonpegel, und der Warteraum|**Rot heißt auf Sendung**, mit Meeting und Mikrofonen.|**Wer im Meeting ist**, jeweils mit Live-Mikrofonpegel.|**Der Warteraum**: Eine Berührung lässt eine Referentin ein.}}

## Regeln für die Routine

Die Faculty einlassen, sobald sie ankommt, den Warteraum so halten, wie er eingestellt wurde, einen Clip nach dem Neustart eines PCs wieder an seine Stelle setzen, den Saal stummschalten, wenn ein Video läuft: Regeln reagieren auf das, was im Meeting, in OBS und an den Mikrofonen geschieht, und tun es jedes Mal gleich. Zu jeder Regel sehen Sie, wann sie zuletzt lief und warum.

{{story:rule|Animation: Dr. Elena Ortega betritt den Warteraum von Saal A, die Regel „Automatisch zulassen“ leuchtet auf, und sie erscheint im Meeting}}

{{loop:director-clip|Einen Clip auf Sendung geben: Das Mikrofon des Saals schaltet sich von selbst stumm.|Bildschirmaufnahme von Director: Der Operator legt den Clip in Saal A auf Program, der Saal wechselt auf VOD und sein Mikrofon wird stumm; zurück im Meeting öffnet es sich wieder}}

## Konnektoren statt fester Technik

Director spricht mit jedem Werkzeug über einen Konnektor, so sind Video, Audio und Meeting-Plattform eine Wahl:

- **OBS Studio**: Szenen, Quellen, Ausgänge und Audio auf jedem Saal-PC
- **NDI**: Video und Audio zwischen den PCs, mit einer Multiview aller Säle
- **Spectacast Meet, Mic und Translator**: das Meeting als einzelne Signale, Telefone als Mikrofone, Live-Übersetzung
- **Sennheiser EW-DX**: die Funkmikrofone des Saals, mit Pegel und Akku
- **MIDI und Ordner**: Bedienpulte und die Clips, die während der Veranstaltung laufen
- **Dante**: das Netzwerk-Audio des Saals, über Dante Virtual Soundcard auf einem PC
- **Ihre eigenen**: jedes Gerät, das HTTP, OSC oder einfache Sockets spricht

Wie Sie ein eigenes Gerät anbinden, Regeln per Skript erweitern und die API nutzen: [Zum Erweitern gebaut](/de/entwickler/).

## Für den Saal gebaut

Director läuft auf einem PC in der Regie und spricht mit den Saal-PCs über das eigene Netzwerk der Location, so läuft eine Veranstaltung weiter, wenn das Internet ausfällt. Die Flotten-Seite zeigt PC, Meeting und Ausgang jedes Saals auf einen Blick; Panels bestehen aus Bausteinen, ein neuer Saal ist also eine weitere Kopie, kein neues Design. Das Dashboard spricht Deutsch, Englisch, Spanisch und Italienisch.

{{closeup:director-fleet|Nahaufnahme der Flotten-Seite von Director: vier Säle, jeder online und im Meeting, mit Mikrofonpegeln und Warteraum|**Der PC jedes Saals**: online und in seinem Meeting.|**Wer spricht**: ein Balken pro Mikrofon, live.|**Der Warteraum**: von hier aus alle zulassen oder ihn ein- und ausschalten.}}

{{plans:Director,Show,Complete}}

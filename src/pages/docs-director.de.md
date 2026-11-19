# Director-Anleitung

<p class="lede">Vom neuen Regie-PC bis zum ersten Saal auf Sendung in etwa einer halben Stunde.</p>

Sie brauchen einen PC mit Windows 10 oder 11 für die Regie und für jeden Saal einen Windows-PC mit OBS Studio und Spectacast Meet. Alle PCs müssen im selben Netzwerk sein.

## 1. Auf dem Regie-PC installieren

1. Laden Sie Spectacast Setup unter [Downloads](/de/downloads/) herunter und entpacken Sie es.
2. Doppelklicken Sie auf **Setup.cmd**. Windows fragt nach Administratorrechten.
3. Wählen Sie **1, Control room**.
4. Setup installiert Director, öffnet seine Ports in der Firewall und startet ihn. Dann zeigt es einen Code wie `K7QM-3XRB`.
5. Melden Sie sich unter [spectacast.com/account](/account/) an, öffnen Sie Ihre Organisation und geben Sie den Code innerhalb einer Stunde unter **Plan und PCs** ein. Der PC hat jetzt seine Lizenz und, falls Sie noch keinen Plan haben, seine Testphase.

Director startet jetzt bei jeder Anmeldung an diesem PC. Seine Dateien liegen in `C:\ProgramData\Spectacast\director`: die Show in `shows\default.json`, die Einstellungen in `.env` und das Protokoll in `logs\engine.log`.

## 2. Das Dashboard öffnen

Öffnen Sie **http://127.0.0.1:4700** in einem Browser auf diesem PC. Das Sprachmenü oben rechts wechselt zwischen English, Deutsch, Español und Italiano.

Um das Dashboard von einem Tablet oder einem anderen PC zu öffnen, fügen Sie diese zwei Zeilen in `C:\ProgramData\Spectacast\director\.env` ein, melden Sie sich dann ab und wieder an:

```
HOST=0.0.0.0
PIN=<eine eigene PIN>
```

Ohne PIN ist Director im Netzwerk nicht erreichbar. Wer das Dashboard öffnet, gibt die PIN einmal ein. Für jemanden, der die Show fahren, aber nicht ändern soll, fügen Sie `OPERATOR_PIN=<eine andere PIN>` hinzu: Sie öffnet nur die Panels.

## 3. Mit der Beispiel-Show beginnen

1. Klicken Sie im Show-Menü oben auf **Beispiel…**.
2. Wählen Sie das Beispiel mit zwei Räumen.
3. Bestätigen Sie mit **Verwenden**. Das ersetzt die leere Show.

Das Beispiel hat zwei Säle, Raum A und Raum B, jeder mit Meet und OBS. Dazu kommen ein Kanalstreifen pro Saal, die Wall mit beiden Bildschirmen und die Regel, die einen Saal auf Sendung schaltet. Seine Adressen (192.168.1.11 und .12) sind Platzhalter, die Sie im nächsten Schritt ändern.

## 4. Ihr erster Saal

Auf dem Saal-PC:

1. Öffnen Sie in OBS **Werkzeuge > WebSocket-Servereinstellungen**, schalten Sie den Server ein, lassen Sie Port 4455 und setzen Sie ein Passwort.
2. Starten Sie Spectacast Meet und melden Sie sich bei Zoom an.

Im Dashboard, auf der Seite **Geräte**:

1. Klicken Sie unter **Netzwerk durchsuchen** auf **suchen**. Director listet die OBS und Meet auf, die er im Netzwerk findet.
2. Öffnen Sie die OBS-Karte von Raum A und setzen Sie die Adresse auf `ws://<Saal-PC>:4455`. Öffnen Sie dann die Meeting-Karte von Raum A und setzen Sie den Host auf die Adresse des Saal-PCs. Jede Karte wird grün, sobald das Gerät antwortet.
3. Tragen Sie das OBS-Passwort in `.env` als `OBS_PASSWORD=<Passwort>` ein, melden Sie sich dann ab und wieder an.
4. Haben Sie nur einen Saal, entfernen Sie die zwei Geräte von Raum B oder lassen Sie sie: Sie erscheinen offline und tun nichts.

## 5. Auf Sendung

Öffnen Sie **Panels**. Der Kanalstreifen von Raum A zeigt sein Bild, sein Meeting und ob er auf Sendung ist.

1. Starten Sie das Meeting über den Streifen.
2. Drücken Sie **Streaming** auf dem Streifen: OBS beginnt, an die in OBS eingestellte Adresse zu streamen.
3. Drücken Sie erneut **Streaming**, um zu stoppen. **Alle Streams starten** startet alle Säle auf einmal.

In der Testphase können zwei Säle 20 Minuten am Stück auf Sendung sein, und die Bilder tragen eine Test-Markierung. Nach 20 Minuten gehen die Säle von der Sendung; starten Sie Director neu (ab- und wieder anmelden), um es erneut zu versuchen.

{{shot:director-channels|Director mit vier Sälen nebeneinander: wer in jedem Meeting ist, der Warteraum, Preview und Program}}

## Wie es weitergeht

- **Weitere Säle:** Fügen Sie OBS und Meet jedes Saals unter **Geräte** hinzu und kopieren Sie einen Kanalstreifen unter **Panels**.
- **Regeln:** Unter **Regeln** zeigt jede Regel, was sie auslöst, was sie tut und wann sie zuletzt lief. Beginnen Sie mit den Regeln des Beispiels und passen Sie sie an.
- **Mic und Translator:** Sie erscheinen unter **Geräte** wie jedes andere Gerät. Siehe die Anleitungen zu [Mic](/de/hilfe/mic/) und [Translator](/de/hilfe/translator/).
- **Jede Seite im Detail:** [Geräte und Treiber](/de/hilfe/director-devices/), [Ihr eigener Treiber](/de/hilfe/director-drivers/), [Panels](/de/hilfe/director-panels/), [Regeln und Skripte](/de/hilfe/director-rules/) und [API, Webhooks und Stream Deck](/de/hilfe/director-api/).

## Wenn etwas nicht funktioniert

- **Eine Karte bleibt rot:** Die Adresse ist falsch, oder die Firewall des Saal-PCs blockiert den Port. Klicken Sie auf die Karte, um den letzten Fehler zu sehen.
- **„keine Lizenz für die Sendung“:** Aktivieren Sie den PC (Schritt 1.5). Die Kopfzeile sagt, warum keine Lizenz da ist.
- **Nichts unter http://127.0.0.1:4700:** Schauen Sie in `C:\ProgramData\Spectacast\director\logs\engine.log`.
- **Das Beispiel rückgängig machen:** **Neu…** im Show-Menü beginnt eine leere Show; **Exportieren** sichert vorher die aktuelle.

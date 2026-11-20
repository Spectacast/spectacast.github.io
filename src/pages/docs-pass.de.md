# Pass-Anleitung

<p class="lede">Richten Sie eine Veranstaltung in Pass ein, machen Sie Telefone zu Scannern an den Zugängen und erhalten Sie danach die Anwesenheit. Pass läuft im Browser, unter spectacast.com/pass.</p>

## 1. Die Veranstaltung

Melden Sie sich unter [spectacast.com/pass](/pass/) mit Ihrem Spectacast-Konto an und legen Sie eine **Neue Veranstaltung** an. Dann, unter **Einrichtung**:

- **Zonen:** die Säle und Räume, in denen die Anwesenheit gezählt wird.
- **Zugänge:** einer pro Eingang, jeder in einer Zone.
- **Sitzungen:** das Programm. Markieren Sie mit **Zählt** die Sitzungen, die für die Anwesenheit zählen.
- **Kategorien:** die Arten von Teilnehmenden, etwa Faculty, Delegierte oder Personal.

Die Checkliste oben sagt, was noch fehlt.

## 2. Teilnehmende und Badges

Unter **Teilnehmende**:

- **+ Person oder Import** fügt jemanden von Hand hinzu, etwa wer sich am Empfang anmeldet, oder liest eine CSV-Datei oder eine als CSV gespeicherte Excel-Datei, mit Spaltenköpfen wie First name, Last name, Email, Category und ID (italienische gehen auch, ebenso Vorname und Nachname). Weitere Spalten bleiben als Felder erhalten, die Regeln und Meldungen nutzen können. Ein erneuter Import aktualisiert dieselben Personen.
- **Feeds** holen die Liste selbstständig von einer Anmeldeseite, und **Schlüssel für andere Systeme** lassen eine Seite ihre Anmeldungen senden. Bitten Sie den Anbieter Ihrer Anmeldeseite oder uns, sie zu verbinden.

Jede Person erhält ein Badge mit QR-Code. **Alle Badges drucken** druckt sie, auf Ihrem eigenen Hintergrund, wenn Sie einen hochladen, oder **Badges per E-Mail** schickt jeder Person ihres.

## 3. Die Zugänge

Nutzen Sie an jedem Zugang ein Telefon oder Tablet oder einen Tastatur-Scanner an einem Laptop.

1. Drücken Sie unter **Einrichtung**, **Zugänge** für den Zugang auf **Telefon einrichten**.
2. Richten Sie die Kamera des Telefons auf den QR-Code am Bildschirm und öffnen Sie den Link. Die Einlass-App öffnet sich auf diesem Zugang, ohne etwas einzutippen.
3. Fügen Sie sie zum Startbildschirm hinzu, damit sie sich wie eine App öffnet.

Der Zugang beantwortet jedes Badge sofort, bildschirmfüllend in Grün, Gelb oder Rot, mit einem Ton und dem Namen der Person. Fällt das Netzwerk aus, entscheidet der Zugang selbst weiter und sendet seine Scans, wenn das Netzwerk zurück ist.

{{closeup:pass-answers|Die drei Antworten des Zugangs, je auf einem Telefon: Grün für einen Eingang mit dem Namen der Person, Gelb, wenn ein Badge gelesen wird, das schon drinnen ist, mit einer Taste zum Fortfahren, und Rot für ein Badge, das nicht gefunden wird|**Grün**: herein, mit Namen begrüßt.|**Gelb**: erst hinsehen. Dieses Badge ist schon drinnen, und der Zugang wartet auf ein Tippen.|**Rot**: ungültig, mit dem nächsten Schritt.}}

Ein **Tastatur-Scanner** funktioniert auf derselben Seite des Zugangs: Stellen Sie ihn so ein, dass er nach jedem Code Enter sendet. Ein Scanner im Speichermodus, an einem Zugang ohne Bildschirm, wird später unter **Scans hochladen** ausgelesen.

## 4. Regeln

Was ein Zugang sagt, entscheiden die **Regeln**, von oben nach unten geprüft; die erste, die passt, entscheidet. Eine neue Veranstaltung beginnt mit sinnvollen Regeln: doppeltes Lesen ignorieren, unbekannte oder stornierte Badges abweisen, warnen, wenn jemand schon drin ist, einen vollen Raum abweisen, alle anderen willkommen heißen. Fügen Sie eigene hinzu, etwa einen Raum nur für eine Kategorie, und probieren Sie jedes Badge mit **Scan testen** aus, bevor die Türen öffnen.

## 5. Während der Veranstaltung

**Live** zeigt, wie viele Personen in jedem Raum sind, die letzten Scans, die Telefone an den Zugängen und ob sie online sind. Was ein Zugang offline anders entschieden hat als der Server, steht unter **Zu prüfen**.

## 6. Danach

**Berichte** liefern pro Person die Minuten und den Anteil in jeder Sitzung, bereit für Excel. Unter **Bescheinigungen** legen Sie fest, was eine Person für eine Teilnahmebescheinigung braucht; wer es erfüllt, lädt seine herunter.

# Datenschutzerklärung

Zuletzt aktualisiert am {{date}}

Diese Erklärung beschreibt, welche personenbezogenen Daten Spectacast verarbeitet, warum, und welche Rechte Sie haben. Sie gilt für die Website spectacast.com, das Spectacast-Kundenkonto, Spectacast Pass, Spectacast Translator und die Lizenzprüfung in Spectacast Director, Meet und Mic. Die Telefon-App Spectacast Mic hat eine eigene kurze Erklärung, die am Ende verlinkt ist.

## Wer wir sind

**Spectacast** ist Verantwortlicher für die hier beschriebenen Daten, sofern ein Abschnitt nichts anderes sagt. Kontakt für Datenschutz: {{PRIVACY_EMAIL}}.

## Kurz gesagt

- Der größte Teil von Spectacast läuft auf den eigenen Computern unserer Kunden. Video, Ton und Meetings einer Veranstaltung bleiben dort, und wir erhalten sie nicht.
- Drei Teile senden Daten ins Internet: **Spectacast Pass**, das wir hosten, **Spectacast Translator**, das Sprache an eine externe KI-Engine sendet, und **Spectacast Meet**, das sich über unseren Server bei Ihrem Zoom-Konto anmeldet.
- Für Daten über die Personen einer Veranstaltung (Teilnehmer, Sprecher) **ist der Veranstalter der Verantwortliche, und wir handeln als sein Auftragsverarbeiter** (Art. 28 DSGVO).
- Wir verkaufen keine personenbezogenen Daten, zeigen keine Werbung und verwenden keine Tracking-Cookies.

## 1. Unsere Kunden: Konto, Abrechnung und Support

| Daten | Zweck | Rechtsgrundlage | Speicherdauer |
|---|---|---|---|
| Name, E-Mail-Adresse, Organisation (falls vorhanden), Land, Ihr Plan | Führung Ihres Kontos und Ihrer Lizenz | Vertrag (Art. 6 Abs. 1 lit. b) | Solange Sie Kunde sind, danach 12 Monate |
| Bestell- und Zahlungsunterlagen | Buchhaltung und Steuern | Rechtliche Verpflichtung (Art. 6 Abs. 1 lit. c) | 10 Jahre (Handelsgesetzbuch und Abgabenordnung) |
| E-Mails und Supportanfragen | Um Ihnen zu antworten | Vertrag, berechtigtes Interesse (Art. 6 Abs. 1 lit. f) | 24 Monate nach der letzten Nachricht |

**Paddle.com** verkauft Spectacast als unser Wiederverkäufer und Merchant of Record. Paddle erhebt Ihre Zahlungsdaten, Ihre Rechnungsadresse und Ihre Steuernummer direkt und ist dafür nach seiner eigenen [Datenschutzerklärung](https://www.paddle.com/legal/privacy) verantwortlich. Wir erhalten von Paddle Ihren Namen, Ihre E-Mail-Adresse, Ihr Land, was Sie gekauft haben und den Zahlungsstatus, niemals Ihre Kartennummer.

## 2. Die Lizenzprüfung (Director, Meet, Mic-Empfänger, Translator)

Die installierten Programme kontaktieren unseren Lizenzserver beim Start und von Zeit zu Zeit. Sie senden den Schlüssel des Computers, die Kennung, die Windows dem Computer gibt (wir speichern nur einen Hash davon), den Namen des Computers und die Programmversion. Unser Server sieht die IP-Adresse des Computers. Wir nutzen diese Daten, um zu prüfen, ob der Plan aktiv ist und wie viele Säle genutzt werden (Vertrag, Art. 6 Abs. 1 lit. b), und bewahren das Protokoll 12 Monate auf. Einmal täglich melden sie außerdem Summen der Nutzung, ohne Inhalte der Veranstaltung: Minuten auf Sendung, Translator-Minuten je Sprache und gescannte Badges. Wenn zu Ihrer Bestellung eine Erstattung oder ein Zahlungsstreit eröffnet wird, dürfen wir Paddle eine Zusammenfassung dieses Protokolls geben, etwa die aktivierten Computer und die Nutzungsstunden, um zu zeigen, ob der Plan genutzt wurde (berechtigtes Interesse, Art. 6 Abs. 1 lit. f).

Wenn Sie Spectacast Meet bei Zoom anmelden, läuft die Anmeldung über unseren Server. Er speichert Ihren Zoom-Namen und Ihre E-Mail-Adresse, Ihre Zoom-Benutzer- und Kontonummer sowie die Berechtigung, die Zoom Meet zum Hosten Ihrer Meetings erteilt, damit der Saalcomputer das Meeting auf Ihrem Konto hosten kann (Vertrag, Art. 6 Abs. 1 lit. b). Wir löschen diese Daten, wenn Sie Meet von Zoom trennen.

## 3. Spectacast Pass: Teilnehmerdaten

Pass wird von uns für den Veranstalter gehostet. **Der Veranstalter ist der Verantwortliche** für die Teilnehmerdaten und entscheidet, was erhoben wird und warum; **wir verarbeiten sie in seinem Auftrag**, nur nach seinen Weisungen, auf Grundlage eines Vertrags zur Auftragsverarbeitung, den wir auf Anfrage zusenden ({{PRIVACY_EMAIL}}).

Daten, die ein Veranstalter typischerweise in Pass führt:

- Name, E-Mail-Adresse, Organisation, Kategorie (zum Beispiel Referent, Teilnehmer, Personal) und Badge-Code des Teilnehmers;
- die Zeiten, zu denen jedes Badge an jedem Eingang gescannt wurde, und die daraus berechneten Sitzungen und Aufenthaltszeiten je Raum;
- Teilnahmebescheinigungen, die aus diesen Aufzeichnungen erstellt werden;
- die Namen der Mitarbeiter des Veranstalters, die die Verwaltungsseiten und die Scanner an den Eingängen nutzen.

Wo sie gespeichert werden: auf Servern der **Hetzner Online GmbH** in der Europäischen Union. Die Telefone an den Eingängen halten Scans offline vor, bis sie sie senden können, und behalten danach nur, was die Scanner-Anzeige braucht.

Wie lange: Das bestimmt der Veranstalter. Standardmäßig werden Veranstaltungsdaten 24 Monate nach der Veranstaltung aufbewahrt, was die Nachweise für die ärztliche Fortbildung (CME) abdeckt, und gelöscht, wenn der Veranstalter die Veranstaltung löscht oder 30 Tage nach dem Ende seines Plans.

Teilnehmer, die ihre Daten einsehen, berichtigen oder löschen lassen möchten, wenden sich an den Veranstalter. Schreiben sie uns, leiten wir die Anfrage an den Veranstalter weiter.

## 4. Spectacast Translator: Sprache, die an KI-Engines gesendet wird

Translator nimmt den Ton eines Mikrofons, eines Saalsignals oder eines Meetings auf und gibt eine Live-Übersetzung zurück. Dafür **wird die Sprache live über eine verschlüsselte Verbindung an die für diese Sprache gewählte KI-Engine gesendet**:

- **Google** (Gemini API), Google Ireland Limited / Google LLC, oder
- **OpenAI** (Realtime API), OpenAI Ireland Ltd / OpenAI, L.L.C.

Die Engine liefert übersetzten Ton und ein schriftliches Transkript zurück. Translator zeigt das Transkript auf dem Bildschirm des Operators und speichert es im Protokoll des Programms auf dem Saalcomputer; es sendet weder Ton noch Transkripte an uns.

Solange die Prüfung auf Sinnumkehr eingeschaltet ist, sendet Translator außerdem das schriftliche Transkript der letzten Minute an ein Textmodell, das die Stellen markiert, an denen die Übersetzung etwas anderes sagt als die sprechende Person: ein Modell von Google oder, wenn der Kunde einen Anthropic-Schlüssel auf dem Computer hinterlegt hat, von Anthropic (Anthropic, PBC). Die Prüfung lässt sich für jede Spur ausschalten.

Wenn der Plan Übersetzungsminuten enthält, nutzt das Programm **unser** Konto bei der Engine: Die Engine verarbeitet die Sprache als unser Unterauftragsverarbeiter, und **wir handeln als Auftragsverarbeiter für den Veranstalter**, der Verantwortlicher für die Stimmen der Sprecher ist. Wenn der Kunde **seine eigenen** API-Schlüssel für die Engine verwendet, schließt er den Vertrag direkt mit der Engine, und wir erhalten nichts.

Was die Engines damit tun: Nach ihren API-Bedingungen in der am 17. November 2026 veröffentlichten Fassung verwenden weder Google noch OpenAI diese API-Daten zum Training ihrer allgemeinen Modelle. Beide bewahren sie für begrenzte Zeit auf, um Missbrauch zu erkennen, und löschen sie dann: OpenAI bis zu 30 Tage, Google bis zu 55 Tage. Die optionale Protokollierung von Anfragen in unserem Google-Projekt lassen wir ausgeschaltet. Ihre Server können außerhalb der EU stehen (auch in den Vereinigten Staaten); Übermittlungen stützen sich auf das EU-US Data Privacy Framework und die Standardvertragsklauseln der Europäischen Kommission.

Sprache kann personenbezogene Daten enthalten, in medizinischen Vorträgen auch Gesundheitsdaten (Art. 9 DSGVO). Der Veranstalter muss die Sprecher darüber informieren, dass ihre Sprache von einer externen KI-Engine übersetzt wird, und darf keine Sprache übersetzen lassen, die er nicht verarbeiten darf. Der Veranstalter kann Translator für jeden Sprecher ausschalten.

## 5. Die Website spectacast.com

Unser Server speichert bei jedem Besuch IP-Adresse, Seite, Datum und Browser in seinem Zugriffsprotokoll, um die Website sicher und funktionsfähig zu halten (berechtigtes Interesse, Art. 6 Abs. 1 lit. f), und löscht das Protokoll nach 14 Tagen. Die Website setzt keine Cookies und nutzt weder Analyse noch Werbung. Ihr Konto und die Verwaltungsseiten von Pass speichern ein Anmelde-Cookie in Ihrem Browser, das für ihre Funktion nötig ist.

## 6. Wer sonst Daten erhält

- **Paddle.com** (Merchant of Record): Bestellungen, Zahlungen, Rechnungen, Steuern.
- **Hetzner Online GmbH**, Deutschland: Hosting von Pass, des Lizenzservers und dieser Website.
- **Google** und **OpenAI**: zu übersetzende Sprache, wie oben beschrieben.
- **Brevo** (Sendinblue SAS), Frankreich: versendet die E-Mails Ihres Kontos und die Badges, die Pass per E-Mail an Teilnehmer schickt.
- **Porkbun, LLC**, Vereinigte Staaten: leitet E-Mails an unsere spectacast.com-Adressen an unser Postfach weiter.
- Unser Steuerberater und unsere Anwälte sowie Behörden, wenn das Gesetz es verlangt.

Jeder Anbieter arbeitet auf Grundlage eines Vertrags, der die Daten schützt. Eine aktuelle Liste der Unterauftragsverarbeiter erhalten Sie auf Anfrage.

## 7. Sicherheit

Daten werden verschlüsselt übertragen (HTTPS). Pass-Daten liegen auf Servern in der EU, der Zugriff ist auf die Personen beschränkt, die den Dienst betreiben, durch Schlüssel geschützt, und sie werden jede Nacht gesichert. Telefon-Mikrofone sind mit dem Computer, mit dem sie sprechen, gekoppelt und Ende-zu-Ende verschlüsselt.

## 8. Ihre Rechte

Nach der DSGVO können Sie von uns Auskunft über Ihre Daten, ihre Berichtigung oder Löschung, die Einschränkung ihrer Verarbeitung und ihre Herausgabe in einem übertragbaren Format verlangen und der Verarbeitung widersprechen. Wo wir uns auf eine Einwilligung stützen, können Sie sie jederzeit widerrufen. Schreiben Sie an {{PRIVACY_EMAIL}}: Wir antworten innerhalb eines Monats. Sie können sich auch bei einer Datenschutz-Aufsichtsbehörde beschweren, insbesondere an Ihrem Wohn- oder Arbeitsort.

Für Daten in Pass oder in einer übersetzten Sitzung ist der Veranstalter der Verantwortliche: Wenden Sie sich zuerst an ihn.

## 9. Kinder

Spectacast ist ein Werkzeug für Veranstaltungen. Es richtet sich nicht an Kinder, und nur Volljährige können einen Plan kaufen.

## 10. Änderungen

Wenn sich diese Erklärung ändert, veröffentlichen wir die neue Fassung hier mit neuem Datum und informieren Kunden per E-Mail, wenn die Änderung wesentlich ist.

Die Datenschutzerklärung der Telefon-App Spectacast Mic: {{MIC_PRIVACY_URL}}.

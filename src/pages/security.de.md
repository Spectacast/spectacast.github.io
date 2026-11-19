# Sicherheit und Daten

<p class="lede">Der größte Teil von Spectacast läuft auf Ihren eigenen Rechnern, im Saal. Diese Seite sagt in einfachen Worten, was dort bleibt, was ins Internet geht und wer damit umgeht. Verbindlich ist die <a href="{{PRIVACY_URL}}">Datenschutzerklärung</a>.</p>

## Was im Saal bleibt

Director, Meet und der Mic-Empfänger sind Programme auf Ihren Saal-PCs. Bild, Ton und die Signale des Meetings laufen zwischen diesen PCs über das Netzwerk des Veranstaltungsorts, und Aufzeichnungen sind Dateien auf Ihren eigenen Festplatten. Wir erhalten nichts davon.

Telefone als Mikrofone werden mit dem PC gekoppelt, mit dem sie sprechen, und ihr Ton ist auf dem Weg Ende-zu-Ende verschlüsselt.

Das Online-Meeting selbst ist ein gewöhnliches Zoom-Meeting, auf Ihrem eigenen Zoom-Konto und zu den Bedingungen von Zoom.

## Was ins Internet geht

| Was | Wohin | Warum |
|---|---|---|
| **Lizenzprüfung:** der Lizenzschlüssel, eine zufällige Kennung des PCs, das Programm und seine Version, der Saal und ob er auf Sendung ist | Unser Lizenzserver in der Europäischen Union | Um zu prüfen, ob Ihr Plan aktiv ist und wie viele Säle in Gebrauch sind |
| **Ihr Konto:** Name, E-Mail-Adresse, Organisation, Land, Plan | Unser Kontoserver in der Europäischen Union | Um Ihr Konto und Ihre Lizenzen zu führen |
| **Spectacast Pass:** Teilnehmer, Badges, Scans an den Eingängen, Anwesenheit | Unser Pass-Server in der Europäischen Union | Pass wird von uns für den Veranstalter gehostet |
| **Spectacast Translator:** die zu übersetzende Sprache | Google oder OpenAI, je nachdem, welchen Dienst Sie für eine Sprache wählen | Der Dienst liefert die Übersetzung live zurück |
| **Ein Bericht**, wenn Sie auf „Bericht senden“ klicken: die Protokolle und Versionen des Programms | Unser Server in der Europäischen Union | Um einen Fehler zu finden; innerhalb von 90 Tagen gelöscht |
| **Zahlungen** | Paddle, das Spectacast als Merchant of Record verkauft | Paddle nimmt die Zahlung entgegen; wir sehen Ihre Kartennummer nie |

Der Inhalt Ihrer Veranstaltung ist nie Teil der Lizenzprüfung. Die Website setzt keine Cookies und verwendet weder Analyse noch Werbung.

## Wenn das Internet ausfällt

Ein Saal, der die Verbindung verliert, läuft weiter: Eine bezahlte Lizenz funktioniert 14 Tage ohne Internet. Die Telefone an den Eingängen entscheiden bei Pass selbstständig weiter und senden ihre Scans, sobald das Netz wieder da ist.

## Wie die Daten geschützt sind

- Jede Verbindung zu unseren Servern ist verschlüsselt (HTTPS).
- Passwörter werden nur als gesalzene Hashes gespeichert, nie im Klartext.
- Die Server stehen in der Europäischen Union; Zugriff haben nur die Personen, die den Dienst betreiben.
- Die Datenbanken von Pass und der Konten werden jede Nacht gesichert.
- Sprache für die Dienste von Translator wird über eine verschlüsselte Verbindung gesendet, und nach ihren API-Bedingungen nutzen weder Google noch OpenAI sie zum Training ihrer allgemeinen Modelle.

## Wer für uns Daten verarbeitet

| Anbieter | Wofür | Wo |
|---|---|---|
| **Hetzner Online GmbH** | Hosting von Pass, des Konto- und Lizenzservers und dieser Website | Europäische Union |
| **Google (Gemini API) und OpenAI (Realtime API)** | Sprachübersetzung, wenn Sie die im Plan enthaltenen Minuten nutzen | Auch außerhalb der Europäischen Union möglich, einschließlich der Vereinigten Staaten |
| **Brevo (Sendinblue SAS)** | Versand der E-Mails Ihres Kontos und der Badges, die Pass per E-Mail an Teilnehmer schickt | Frankreich |
| **Porkbun, LLC** | Weiterleitung von E-Mails an unsere spectacast.com-Adressen | Vereinigte Staaten |

Paddle steht nicht auf dieser Liste, weil es Ihre Zahlungsdaten als eigener Verantwortlicher verarbeitet. Wenn Sie Translator mit Ihrem eigenen Schlüssel von Google oder OpenAI nutzen, schließen Sie den Vertrag direkt mit dem Dienst, und wir erhalten nichts.

## Die Daten Ihrer Teilnehmer

Für die Personen Ihrer Veranstaltung sind Sie der Verantwortliche und wir Ihr Auftragsverarbeiter (Art. 28 DSGVO). Wir verarbeiten ihre Daten nur nach Ihren Weisungen, und Sie entscheiden, wie lange Pass sie aufbewahrt. Den Vertrag zur Auftragsverarbeitung senden wir auf Anfrage: Schreiben Sie an [privacy@spectacast.com](mailto:privacy@spectacast.com).

Wie lange jede Art von Daten aufbewahrt wird, steht in der [Datenschutzerklärung]({{PRIVACY_URL}}).

## Ein Sicherheitsproblem melden

Wenn Sie eine Schwachstelle in Spectacast finden, schreiben Sie an [support@spectacast.com](mailto:support@spectacast.com), bevor Sie sie veröffentlichen, damit wir sie zuerst beheben können.

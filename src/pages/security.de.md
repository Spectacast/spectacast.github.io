# Sicherheit und Daten

<p class="lede">Der größte Teil von Spectacast läuft auf Ihren eigenen Rechnern, im Saal. Diese Seite sagt in einfachen Worten, was dort bleibt, was ins Internet geht und wer damit umgeht. Verbindlich ist die <a href="{{PRIVACY_URL}}">Datenschutzerklärung</a>.</p>

## Was im Saal bleibt

Director, Meet und der Mic-Empfänger sind Programme auf Ihren Saal-PCs. Bild, Ton und die Signale des Meetings laufen zwischen diesen PCs über das Netzwerk des Veranstaltungsorts, und Aufzeichnungen sind Dateien auf Ihren eigenen Festplatten. Wir erhalten nichts davon.

Telefone als Mikrofone werden mit dem PC gekoppelt, mit dem sie sprechen, und ihr Ton wird Ende-zu-Ende verschlüsselt übertragen.

Das Online-Meeting selbst ist ein gewöhnliches Zoom-Meeting, auf Ihrem eigenen Zoom-Konto und zu den Bedingungen von Zoom.

## Was ins Internet geht

| Was | Wohin | Warum |
|---|---|---|
| **Lizenzprüfung:** der Schlüssel des PCs, die Kennung, die Windows dem PC gibt (wir speichern nur einen Hash davon), der Name des PCs, die Programmversion und Tagessummen der Nutzung: Minuten auf Sendung, Translator-Minuten je Sprache, gescannte Badges | Unser Kontoserver in der Europäischen Union | Um zu prüfen, ob Ihr Plan aktiv ist, wie viele PCs in Gebrauch sind und wie viele Übersetzungsminuten verbraucht wurden |
| **Ihr Konto:** Name, E-Mail-Adresse, Organisation, Land, Plan | Unser Kontoserver in der Europäischen Union | Um Ihr Konto und Ihre Lizenzen zu führen |
| **Zoom-Anmeldung von Meet:** Ihr Zoom-Name, Ihre E-Mail-Adresse und die Berechtigung, Ihre Meetings zu hosten | Unser Server in der Europäischen Union | Damit Meet das Meeting auf Ihrem Zoom-Konto hosten kann; entfernt, wenn Sie Meet von Zoom trennen |
| **Spectacast Pass:** Teilnehmer, Badges, Scans an den Eingängen, Anwesenheit | Unser Pass-Server in der Europäischen Union | Pass wird von uns für den Veranstalter gehostet |
| **Spectacast Translator:** die zu übersetzende Sprache | Google oder OpenAI, je nachdem, welche Engine Sie für eine Sprache wählen | Die Engine liefert die Übersetzung live zurück |
| **Translators Prüfung auf Sinnumkehr**, solange sie eingeschaltet ist: die Mitschrift der letzten Minute als Text | Google, oder Anthropic, wenn Sie dessen Schlüssel auf dem PC hinterlegen | Um die Stellen zu markieren, an denen die Übersetzung etwas anderes sagt als die sprechende Person |
| **Zahlungen** | Paddle, das Spectacast als Merchant of Record verkauft | Paddle nimmt die Zahlung entgegen; wir sehen Ihre Kartennummer nie |

Der Inhalt Ihrer Veranstaltung ist nie Teil der Lizenzprüfung. Diese Website setzt keine Cookies und verwendet weder Analyse noch Werbung; die Anmeldung bei Ihrem Konto oder bei Pass speichert ein Anmelde-Cookie, das dafür nötig ist.

## Wenn das Internet ausfällt

Die Säle und die Regie arbeiten über das Netzwerk des Veranstaltungsorts weiter, und eine bezahlte Lizenz funktioniert 14 Tage ohne Internet. Das Online-Meeting und die Übersetzung brauchen das Internet. Die Telefone an den Eingängen entscheiden bei Pass selbstständig weiter und senden ihre Scans, sobald das Netz wieder da ist.

## Wie die Daten geschützt sind

- Jede Verbindung zu unseren Servern ist verschlüsselt (HTTPS).
- Passwörter werden nur als gesalzene Hashes gespeichert, nie im Klartext.
- Die Server stehen in der Europäischen Union; Zugriff haben nur die Personen, die den Dienst betreiben.
- Die Datenbanken von Pass und der Konten werden jede Nacht gesichert.
- Sprache für die Engines von Translator wird über eine verschlüsselte Verbindung gesendet, und nach ihren API-Bedingungen nutzen weder Google noch OpenAI sie zum Training ihrer allgemeinen Modelle.

## Wer für uns Daten verarbeitet

| Anbieter | Wofür | Wo |
|---|---|---|
| **Hetzner Online GmbH** | Hosting von Pass, des Konto- und Lizenzservers und dieser Website | Europäische Union |
| **Google (Gemini API) und OpenAI (Realtime API)** | Sprachübersetzung, wenn Sie die im Plan enthaltenen Minuten nutzen | Auch außerhalb der Europäischen Union möglich, einschließlich der Vereinigten Staaten |
| **Brevo (Sendinblue SAS)** | Versand der E-Mails Ihres Kontos und der Badges, die Pass per E-Mail an Teilnehmer schickt | Frankreich |
| **Porkbun, LLC** | Weiterleitung von E-Mails an unsere spectacast.com-Adressen | Vereinigte Staaten |

Paddle steht nicht auf dieser Liste, weil es Ihre Zahlungsdaten als eigenständiger Verantwortlicher verarbeitet. Wenn Sie Translator mit Ihrem eigenen Schlüssel von Google oder OpenAI nutzen, schließen Sie den Vertrag direkt mit der Engine, und wir erhalten nichts.

## Die Daten Ihrer Teilnehmer

Für die Personen Ihrer Veranstaltung sind Sie der Verantwortliche und wir Ihr Auftragsverarbeiter (Art. 28 DSGVO). Wir verarbeiten ihre Daten nur nach Ihren Weisungen. Den Vertrag zur Auftragsverarbeitung senden wir auf Anfrage: Schreiben Sie an [privacy@spectacast.com](mailto:privacy@spectacast.com).

Wie lange jede Art von Daten aufbewahrt wird, steht in der [Datenschutzerklärung]({{PRIVACY_URL}}).

## Ein Sicherheitsproblem melden

Wenn Sie eine Schwachstelle in Spectacast finden, schreiben Sie an [support@spectacast.com](mailto:support@spectacast.com), bevor Sie sie veröffentlichen, damit wir sie zuerst beheben können.

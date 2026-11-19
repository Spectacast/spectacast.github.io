# Meet-Anleitung

<p class="lede">Spectacast Meet tritt dem Online-Meeting vom Saal-PC aus bei und macht aus jeder teilnehmenden Person, der Galerie und jeder Bildschirmfreigabe ein Videosignal für den Saal.</p>

## Was Sie brauchen

- Einen Windows-PC im Saal, im selben Netzwerk wie die Regie.
- Ein Zoom-Konto, das das Meeting veranstalten kann.
- OBS Studio auf demselben PC oder ein Mischer, der NDI empfängt.

## Installieren und anmelden

1. Starten Sie Spectacast Setup auf dem Saal-PC und wählen Sie **Hall PC**. Setup installiert, was der Saal-PC ausführt, darunter Meet, und zeigt einen Code, mit dem Sie den PC in Ihrem Konto unter **Plan und PCs** als Saal-PC aktivieren.
2. Starten Sie Meet. Sein Bedienfeld öffnet sich in einem eigenen Fenster; das Symbol im Infobereich holt es zurück.
3. Melden Sie sich bei Zoom an und legen Sie unter **Einstellungen** das Meeting fest, das der Saal veranstaltet: die Meeting-Nummer, den Namen, den Meet im Meeting zeigt, sowie Mikrofon und Lautsprecher des Saals.

Meet startet nach einem Neustart des PCs von selbst wieder, mit denselben Einstellungen und Ausgängen.

## Das Bedienfeld

| Reiter | Was er tut |
| --- | --- |
| Meeting | als Host starten oder beitreten, verlassen oder beenden, Chat, alle stummschalten |
| Teilnehmer | stummschalten, Video, Spotlight, Handzeichen, Rollen, umbenennen, Warteraum und Breakout-Räume, und eine Taste pro Ausgang, um jemanden darauf zu legen |
| Ausgänge | wie viele Signale, und für jedes, was es zeigt, in welcher Auflösung, mit welchem Ton |
| Einstellungen | das Meeting, der Name, die Audiogeräte, die Zoom-Anmeldung und das Protokoll |

## Die Signale

Jeder Ausgang ist eine NDI-Quelle im Netzwerk. Wählen Sie für jeden, was er zeigt (die Modi heißen auf Englisch):

- **Participant** (Teilnehmer): eine Person, nach Namen gewählt.
- **Active Speaker** (aktiver Sprecher): wer zuletzt gesprochen hat.
- **Spotlight:** die hervorgehobene Person, oder eine gewählte Person, wenn niemand hervorgehoben ist.
- **Zoom view** (Zoom-Ansicht): das Meeting so angeordnet wie in Zoom, ohne Namen und ohne Zoom-Grafiken: die Freigabe, während jemand teilt, sonst die Galerie oder der Sprecher.

Wählen Sie dann das Bild (die Kamera, oder die Bildschirmfreigabe, wenn es eine gibt) und den Ton: den dieser Person, das ganze Meeting oder das Meeting ohne eine Person, für ein Rücksignal, das der Raum schon hört. Fügen Sie das Signal in OBS als NDI-Quelle hinzu.

## Aus der Regie

In Director erscheint Meet unter **Geräte** wie jedes andere Gerät, und der Kanalstreifen unter **Panels** zeigt, wer im Meeting ist, wer spricht und wer wartet. Von dort lässt die Regie Personen herein, schaltet stumm und legt Sprechende auf einen Ausgang, ohne den Saal-PC anzufassen.

## Dolmetschkanäle

Hat das Meeting Dolmetschen eingerichtet, kann Meet als Dolmetscher einer Sprache beitreten und mit einer Stimme aus [Translator](/de/hilfe/translator/) oder von einer Person in der Kabine sprechen. Die Zuhörenden wählen die Sprache wie gewohnt in Zoom.

{{shot:meet-interpreter-card|Die Karte, die Meet auf einem Dolmetschkanal zeigt: die Sprache und „Live interpretation“}}

## Wenn etwas nicht funktioniert

- **„Cannot connect to Zoom (no internet?)“:** Meet versucht es jede Minute erneut; prüfen Sie das Internet des Saal-PCs.
- **Ein Ausgang ist schwarz:** Niemand passt dazu, etwa weil die gewählte Person gegangen ist. Wählen Sie eine andere Person oder stellen Sie den Ausgang auf Active Speaker.
- **Was Zoom geantwortet hat:** Das Protokoll steht unten unter **Einstellungen**.

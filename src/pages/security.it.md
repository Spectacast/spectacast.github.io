# Sicurezza e dati

<p class="lede">La maggior parte di Spectacast funziona sui tuoi computer, in sala. Questa pagina dice con parole semplici cosa resta lì, cosa va online e chi lo tratta. Il testo vincolante è l'<a href="{{PRIVACY_URL}}">Informativa privacy</a>.</p>

## Cosa resta in sala

Director, Meet e il ricevitore Mic sono programmi installati sui tuoi PC di sala. Il video, l'audio e i flussi della riunione viaggiano tra quei PC sulla rete della sede, e le registrazioni sono file sui tuoi dischi. Noi non riceviamo nulla di tutto questo.

I telefoni usati come microfoni vengono abbinati al PC con cui parlano, e il loro audio viaggia cifrato da un capo all'altro.

La riunione online è una normale riunione Zoom, sul tuo account Zoom e alle condizioni di Zoom.

## Cosa va online

| Cosa | Dove va | Perché |
|---|---|---|
| **Verifica della licenza:** la chiave del PC, l'identificativo che Windows assegna al PC (ne conserviamo solo l'hash), il nome del PC, la versione del programma e i totali giornalieri d'uso: minuti in onda, minuti di Translator per lingua, badge letti | Il nostro server degli account nell'Unione Europea | Per verificare che il piano sia attivo, quanti PC sono in uso e quanti minuti di traduzione sono stati consumati |
| **Il tuo account:** nome, email, organizzazione, paese, piano | Il nostro server degli account nell'Unione Europea | Per gestire il tuo account e le tue licenze |
| **Accesso di Meet a Zoom:** il tuo nome e la tua email di Zoom, e l'autorizzazione a ospitare le tue riunioni | Il nostro server nell'Unione Europea | Perché Meet possa ospitare la riunione sul tuo account Zoom; rimosso quando scolleghi Meet da Zoom |
| **Spectacast Pass:** partecipanti, badge, letture agli ingressi, presenze | Il nostro server di Pass nell'Unione Europea | Pass è ospitato da noi per l'organizzatore dell'evento |
| **Spectacast Translator:** il parlato da tradurre | Google o OpenAI, secondo il motore che scegli per ogni lingua | Il motore restituisce la traduzione dal vivo |
| **Il controllo del senso capovolto di Translator**, finché è attivo: la trascrizione scritta dell'ultimo minuto | Google, oppure Anthropic se ne imposti la chiave sul PC | Per segnalare i punti in cui la traduzione dice altro rispetto al relatore |
| **Pagamenti** | Paddle, che vende Spectacast come Merchant of Record | Paddle incassa il pagamento; non vediamo mai il numero della tua carta |

Il contenuto del tuo evento non fa mai parte della verifica della licenza. Questo sito non usa cookie, né strumenti di analisi o pubblicità; l'accesso al tuo account o a Pass salva un cookie di accesso, necessario per farli funzionare.

## Quando cade internet

Le sale e la regia continuano a lavorare sulla rete della sede, e una licenza a pagamento funziona 14 giorni senza internet. La riunione online e la traduzione hanno bisogno di internet. I telefoni agli ingressi di Pass continuano a decidere da soli e inviano le letture quando la rete torna.

## Come sono protetti i dati

- Ogni connessione ai nostri server è cifrata (HTTPS).
- Le password sono conservate solo come hash con salt, mai in chiaro.
- I server sono nell'Unione Europea, con accesso limitato alle persone che gestiscono il servizio.
- I database di Pass e degli account hanno un backup ogni notte.
- Il parlato inviato ai motori di Translator viaggia su una connessione cifrata, e secondo le loro condizioni API né Google né OpenAI lo usano per addestrare i propri modelli generali.

## Chi tratta dati per noi

| Fornitore | Per cosa | Dove |
|---|---|---|
| **Hetzner Online GmbH** | Hosting di Pass, del server degli account e delle licenze e di questo sito | Unione Europea |
| **Google (Gemini API) e OpenAI (Realtime API)** | Traduzione del parlato, quando usi i minuti inclusi nel piano | Anche fuori dall'Unione Europea, Stati Uniti compresi |
| **Brevo (Sendinblue SAS)** | Invio delle email del tuo account e dei badge che Pass invia per email ai partecipanti | Francia |
| **Porkbun, LLC** | Inoltro delle email inviate ai nostri indirizzi spectacast.com | Stati Uniti |

Paddle non è in questo elenco perché tratta i tuoi dati di pagamento come titolare autonomo. Quando usi Translator con la tua chiave Google o OpenAI, il contratto è direttamente tra te e il motore, e noi non riceviamo nulla.

## I dati dei tuoi partecipanti

Per le persone presenti al tuo evento il titolare sei tu e noi siamo il tuo responsabile del trattamento (art. 28 GDPR). Trattiamo i loro dati solo secondo le tue istruzioni. Inviamo l'accordo sul trattamento dei dati su richiesta: scrivi a [privacy@spectacast.com](mailto:privacy@spectacast.com).

Per quanto tempo si conserva ogni tipo di dato è indicato nell'[Informativa privacy]({{PRIVACY_URL}}).

## Segnalare un problema di sicurezza

Se trovi una vulnerabilità in Spectacast, scrivi a [support@spectacast.com](mailto:support@spectacast.com) prima di renderla pubblica, così possiamo correggerla prima.

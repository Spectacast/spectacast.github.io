# Guida di Director

<p class="lede">Da un PC di regia nuovo alla prima sala in onda in circa mezz'ora.</p>

Ti serve un PC con Windows 10 o 11 per la regia e, per ogni sala, un PC Windows con OBS Studio e Spectacast Meet. Tutti i PC devono essere sulla stessa rete.

## 1. Installare sul PC di regia

1. Scarica Spectacast Setup da [Download](/it/download/) ed estrailo.
2. Fai doppio clic su **Setup.cmd**. Windows chiede i diritti di amministratore.
3. Scegli **1, Control room**.
4. Setup installa Director, apre le sue porte nel firewall e lo avvia. Poi mostra un codice come `K7QM-3XRB`.
5. Accedi a [spectacast.com/account](/account/), apri la tua organizzazione e inserisci il codice in **Piano e PC** entro un'ora. Il PC ha ora la sua licenza e, se non hai ancora un piano, la sua prova.

Director ora si avvia ogni volta che accedi a questo PC. I suoi file sono in `C:\ProgramData\Spectacast\director`: lo show in `shows\default.json`, le impostazioni in `.env` e il log in `logs\engine.log`.

## 2. Aprire la dashboard

Apri **http://127.0.0.1:4700** in un browser su quel PC. Il menu della lingua in alto a destra passa tra English, Deutsch, Español e Italiano.

Per aprire la dashboard da un tablet o da un altro PC, aggiungi queste due righe a `C:\ProgramData\Spectacast\director\.env`, poi esci e rientra in Windows:

```
HOST=0.0.0.0
PIN=<un tuo PIN>
```

Senza PIN, Director non si apre alla rete. Chi apre la dashboard inserisce il PIN una volta. Per chi deve condurre lo show senza modificarlo, aggiungi `OPERATOR_PIN=<un altro PIN>`: apre solo i pannelli.

## 3. Partire dallo show di esempio

1. Nel menu dello show, in alto, fai clic su **Esempio…**.
2. Scegli l'esempio con due sale.
3. Conferma con **Usalo**. Sostituisce lo show vuoto.

L'esempio ha due sale, Sala A e Sala B, ognuna con Meet e OBS. Ha anche una striscia di canale per sala, il Wall con entrambi gli schermi e la regola che manda una sala in onda. I suoi indirizzi (192.168.1.11 e .12) sono segnaposto, che cambi nel passo successivo.

## 4. La tua prima sala

Sul PC di sala:

1. In OBS, apri **Strumenti > Impostazioni del server WebSocket**, attiva il server, lascia la porta 4455 e imposta una password.
2. Avvia Spectacast Meet e accedi con Zoom.

Nella dashboard, nella pagina **Dispositivi**:

1. Fai clic su **cerca** sotto **Cerca nella rete**. Director elenca gli OBS e i Meet che trova in rete.
2. Apri la scheda OBS di Sala A e imposta l'indirizzo `ws://<PC di sala>:4455`. Poi apri la scheda della riunione di Sala A e imposta come host l'indirizzo del PC di sala. Ogni scheda diventa verde quando il dispositivo risponde.
3. Metti la password di OBS in `.env` come `OBS_PASSWORD=<password>`, poi esci e rientra in Windows.
4. Se hai una sola sala, rimuovi i due dispositivi di Sala B, oppure lasciali: risultano offline e non fanno nulla.

## 5. In onda

Apri **Pannelli**. La striscia di canale di Sala A mostra la sua immagine, la sua riunione e se è in onda.

1. Avvia la riunione dalla striscia.
2. Premi **Streaming** sulla striscia: OBS inizia a trasmettere all'indirizzo impostato in OBS.
3. Premi di nuovo **Streaming** per fermare. **Avvia tutti gli stream** manda in onda tutte le sale insieme.

Nella prova, due sale possono stare in onda 20 minuti di fila, e le immagini portano un marchio di prova. Dopo 20 minuti le sale vanno fuori onda; riavvia Director (esci e rientra in Windows) per riprovare.

{{shot:director-channels|Spectacast Director con quattro sale affiancate: chi è in ogni riunione, la sala d'attesa, Preview e Program}}

## E poi

- **Altre sale:** aggiungi l'OBS e il Meet di ogni sala in **Dispositivi**, poi copia una striscia di canale in **Pannelli**.
- **Regole:** in **Regole**, ogni regola dice cosa la avvia e cosa fa, e mostra quando è partita l'ultima volta. Parti dalle regole dell'esempio e modificale.
- **Mic e Translator:** compaiono in **Dispositivi** come ogni altro dispositivo. Vedi le guide di [Mic](/it/guida/mic/) e [Translator](/it/guida/translator/).
- **Ogni pagina in dettaglio:** [Dispositivi e driver](/it/guida/director-devices/), [Il tuo driver](/it/guida/director-drivers/), [Pannelli](/it/guida/director-panels/), [Regole e script](/it/guida/director-rules/) e [API, webhook e Stream Deck](/it/guida/director-api/).

## Quando qualcosa non funziona

- **Una scheda resta rossa:** l'indirizzo è sbagliato, oppure il firewall del PC di sala blocca la porta. Fai clic sulla scheda per vedere l'ultimo errore.
- **«nessuna licenza per andare in onda»:** attiva il PC (passo 1.5). L'intestazione dice perché manca la licenza.
- **Niente su http://127.0.0.1:4700:** guarda `C:\ProgramData\Spectacast\director\logs\engine.log`.
- **Annullare l'esempio:** **Nuovo…** nel menu dello show avvia uno show vuoto; **Esporta** salva prima quello che hai.

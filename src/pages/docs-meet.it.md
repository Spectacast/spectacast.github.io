# Guida di Meet

<p class="lede">Spectacast Meet entra nella riunione online dal PC di sala e trasforma ogni partecipante, la galleria e ogni condivisione dello schermo in un segnale video per la sala.</p>

## Cosa ti serve

- Un PC Windows in sala, sulla stessa rete della regia.
- Un account Zoom che possa ospitare la riunione.
- OBS Studio sullo stesso PC, o un mixer che riceve NDI.

## Installare e accedere

1. Avvia Spectacast Setup sul PC di sala e scegli **Hall PC**. Setup installa ciò che il PC di sala esegue, Meet compreso, e mostra un codice per attivare il PC come PC di sala nel tuo account, in **Piano e PC**.
2. Avvia Meet. Il suo pannello di controllo si apre in una finestra sua; l'icona nell'area di notifica lo riapre.
3. Accedi con Zoom e, in **Impostazioni**, indica la riunione che la sala ospita: il numero della riunione, il nome che Meet mostra nella riunione, il microfono e gli altoparlanti della sala.

Meet riparte da solo dopo un riavvio del PC, con le stesse impostazioni e uscite.

## Il pannello di controllo

| Scheda | Cosa fa |
| --- | --- |
| Riunione | avviare come host o partecipare, uscire o terminare, chat, silenziare tutti |
| Partecipanti | silenziare, video, in evidenza, mani alzate, ruoli, rinominare, sala d'attesa e stanze secondarie, e un pulsante per uscita per metterci qualcuno |
| Uscite | quanti segnali e, per ognuno, cosa mostra, a quale risoluzione, con quale audio |
| Impostazioni | la riunione, il nome, i dispositivi audio, l'accesso a Zoom e il log |

## I segnali

Ogni uscita è una sorgente NDI in rete. Per ognuna, scegli cosa mostra (le modalità sono in inglese):

- **Participant** (partecipante): una persona, scelta per nome.
- **Active Speaker** (chi parla): chi ha parlato per ultimo.
- **Spotlight** (in evidenza): la persona in evidenza, o una persona scelta quando non c'è nessuno in evidenza.
- **Zoom view** (vista Zoom): la riunione disposta come in Zoom, senza nomi né grafica di Zoom: la condivisione mentre qualcuno condivide, altrimenti la galleria o chi parla.

Poi scegli l'immagine (la camera, o la condivisione dello schermo quando c'è) e l'audio: quello di quella persona, di tutta la riunione, o la riunione senza una persona, per un ritorno che la sala sente già. In OBS, aggiungi il segnale come sorgente NDI.

## Dalla regia

In Director, Meet compare in **Dispositivi** come ogni altro dispositivo, e la striscia di canale in **Pannelli** mostra chi è in riunione, chi parla e chi aspetta. Da lì la regia ammette persone, silenzia e mette un relatore su un'uscita, senza toccare il PC di sala.

## Canali di interpretariato

Quando la riunione ha l'interpretariato, Meet può entrare come interprete di una lingua e parlare con una voce di [Translator](/it/guida/translator/) o di una persona in cabina. Chi ascolta sceglie la lingua in Zoom come sempre.

{{shot:meet-interpreter-card|La scheda che Meet mostra su un canale di interpretariato: la lingua e «Interpretazione dal vivo»}}

## Quando qualcosa non funziona

- **«Cannot connect to Zoom (no internet?)»:** Meet riprova ogni minuto; controlla l'internet del PC di sala.
- **Un'uscita è nera:** nessuno corrisponde, ad esempio la persona scelta è uscita. Scegli un'altra persona, o imposta l'uscita su Active Speaker.
- **Cosa ha risposto Zoom:** il log è in fondo a **Impostazioni**.

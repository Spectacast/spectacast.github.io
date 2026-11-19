# Dispositivi e driver

<p class="lede">Tutto ciò che Director controlla è un dispositivo: l'OBS di una sala, la sua riunione, un ricevitore per i telefoni-microfono, un ricevitore radio, un controller MIDI. Un driver dice a Director cosa sa fare un tipo di dispositivo e cosa comunica.</p>

## Aggiungere un dispositivo

1. Apri la pagina **Dispositivi** e fai clic su **Aggiungi dispositivo**.
2. Scegli il driver e scrivi un nome. Il modulo mostra un campo per ogni impostazione che serve al driver, con il suo valore predefinito.
3. Salva. La scheda diventa verde appena il dispositivo risponde. Fai clic su una scheda per vederne lo stato e l'ultimo errore.

**modifica** su una scheda cambia il nome e le impostazioni; Director si ricollega al salvataggio. **Cerca nella rete** e poi **cerca** elenca ogni OBS e ogni Spectacast Meet che risponde in rete; **usa nel modulo** compila il modulo con uno di questi.

Le password non stanno nel file dello show. Mettile in `C:\ProgramData\Spectacast\director\.env`, per esempio `OBS_PASSWORD=<password>`, poi esci dalla sessione e rientra.

## I driver inclusi in Director

| Driver | Cosa vede e cosa fa Director |
|---|---|
| **OBS Studio** | Scene, fonti, audio, registrazione e streaming di un OBS, tramite il suo server WebSocket |
| **NDI discovery** | Le sorgenti NDI in rete, anche attraverso un NDI Discovery Server; le loro immagini nella pagina **Wall** |
| **Spectacast Meet** | Chi è nella riunione e in sala d'attesa; ammettere, silenziare e mettere in evidenza; quale flusso va a quale uscita |
| **Spectacast Mic** | I telefoni collegati a un PC di sala come microfoni e interfono |
| **Translator** | Avviare e fermare una traduzione, scegliere le lingue, leggere ciò che è stato sentito e ciò che è stato detto |
| **Sennheiser EW-DX receiver** | Mute, guadagno, livello, collegamento radio e batteria di ogni canale. Attiva prima l'accesso di terze parti sul ricevitore |
| **MIDI controller** | Note e controller nei due sensi: fader e pulsanti di una superficie di controllo |
| **Folder of files** | I video di una cartella, locale o condivisa; un file copiato dentro compare da solo |
| **Recorder** | Registra il flusso della riunione di una sala in file di un'ora |

Un dispositivo che non è in questo elenco riceve un driver suo nella pagina **Driver**, senza codice: vedi [Il tuo driver](/it/guida/director-drivers/).

## Ingressi dall'esterno

Due ingressi permettono a un altro sistema di avviare qualcosa in Director. Sono entrambi nella pagina **Dispositivi**, sotto **Ingressi**.

- **webhook:** una chiamata a `POST /api/hooks/<name>` genera l'evento `<name>`. Il corpo JSON e i parametri dell'indirizzo arrivano come campi dell'evento.
- **Ingresso OSC:** imposta una porta, e ogni messaggio OSC che vi arriva diventa un evento con il nome del suo indirizzo: `/cue/go` diventa `cue_go`.

Poi una regola reagisce all'evento. Vedi [Regole e script](/it/guida/director-rules/) e [API, webhook e Stream Deck](/it/guida/director-api/).

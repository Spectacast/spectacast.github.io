# Dispositivi e driver

<p class="lede">Tutto ciò che Director controlla è un dispositivo: l'OBS di una sala, la sua riunione, un ricevitore per i telefoni-microfono, un ricevitore radio, un controller MIDI. Un driver dice a Director cosa sa fare un tipo di dispositivo e cosa comunica.</p>

## Aggiungere un dispositivo

1. Apri la pagina **Dispositivi** e vai al modulo **Aggiungi dispositivo**, sotto le schede.
2. Scegli il driver e scrivi un nome. Il modulo mostra un campo per ogni impostazione che serve al driver, con il suo valore predefinito.
3. Fai clic su **Aggiungi**. Il punto sulla scheda diventa verde appena il dispositivo risponde; la scheda ne mostra lo stato e l'ultimo errore.

**modifica** su una scheda cambia il nome e le impostazioni; Director si ricollega al salvataggio. **Cerca nella rete** e poi **cerca** elenca ogni OBS e ogni Spectacast Meet che risponde in rete; **usa nel modulo** compila il modulo con uno di questi.

La password di OBS non sta nel file dello show: mettila in `C:\ProgramData\Spectacast\director\.env` come `OBS_PASSWORD=<password>`, poi esci e rientra in Windows. La password di un ricevitore Sennheiser o di un ricevitore Mic viene salvata nel file dello show.

## I driver inclusi in Director

| Driver | Cosa vede e cosa fa Director |
|---|---|
| **OBS Studio** | Scene, fonti, audio, registrazione e streaming di un OBS, tramite il suo server WebSocket |
| **NDI discovery** | Le sorgenti NDI in rete, anche attraverso un NDI Discovery Server. Un controllo **Anteprima** mostra l'immagine di ognuna |
| **Spectacast Meet** | Chi è nella riunione e in sala d'attesa; ammettere, silenziare e mettere in evidenza; quale flusso va a quale uscita |
| **Spectacast Mic** | I telefoni collegati a un PC di sala come microfoni e interfono |
| **Translator** | Avviare e fermare una traduzione, scegliere le lingue, leggere ciò che è stato sentito e ciò che è stato detto |
| **Sennheiser EW-DX receiver** | Mute, guadagno, livello, collegamento radio e batteria di ogni canale. Attiva prima 3rd Party Access in Sennheiser Control Cockpit (firmware 4.0.0 o successivo) |
| **MIDI controller** | Note e controller nei due sensi: fader e pulsanti di una superficie di controllo |
| **Folder of files** | I clip di una cartella, locale o condivisa; un file copiato dentro compare da solo |
| **Recorder** | Registra il flusso della riunione di una sala in file di un'ora |

Un dispositivo che non è in questo elenco riceve un driver suo nella pagina **Driver**, senza codice: vedi [Il tuo driver](/it/guida/director-drivers/).

## Ingressi dall'esterno

Due ingressi permettono a un altro sistema di avviare qualcosa in Director. Sono entrambi nella pagina **Dispositivi**, sotto **Ingressi**.

- **Webhooks:** una chiamata a `POST /api/hooks/<name>` genera l'evento `<name>`. Il corpo JSON e i parametri dell'indirizzo arrivano come campi dell'evento.
- **Ingresso OSC:** imposta una porta, e ogni messaggio OSC che vi arriva diventa un evento con il nome del suo indirizzo: `/cue/go` diventa `cue_go`.

Poi una regola reagisce all'evento. Vedi [Regole e script](/it/guida/director-rules/) e [API, webhook e Stream Deck](/it/guida/director-api/).

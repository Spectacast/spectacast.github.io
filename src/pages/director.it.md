# Spectacast Director

<p class="lede">La regia per eventi ibridi dal vivo. Una sola dashboard vede insieme tutti i PC di sala, la riunione online e i microfoni, e le regole si occupano di quello che altrimenti qualcuno farebbe a mano, molte volte al giorno.</p>

{{cta}}

{{shot:director-channels|Spectacast Director con quattro sale affiancate: chi è in ogni riunione, la sala d'attesa, Preview e Program}}

## Tutte le sale su uno schermo

Ogni sala ha la sua colonna: chi è nella riunione e chi parla, la sala d'attesa e la lobby, Preview e Program, il banner e lo streaming. Scegli un relatore, lo mandi in onda con un tocco, e la sala successiva è subito accanto. Una sola persona può seguire un intero congresso; al congresso di 18 sale per cui Director è nato, è andata così.

## Regole per la routine

Ammettere la faculty appena arriva, tenere la sala d'attesa come è stata impostata, rimettere un video al suo posto quando un PC riparte, silenziare la sala mentre va un filmato: le regole reagiscono a quello che succede nella riunione, in OBS e sui microfoni, e lo fanno ogni volta allo stesso modo. Per ogni regola vedi quando è partita l'ultima volta e perché.

{{shot:director-rules|Le regole di Director: ognuna con ciò che la fa partire e la sua ultima esecuzione}}

## Connettori, non un impianto fisso

Director parla con ogni strumento tramite un connettore, così video, audio e piattaforma di riunione sono una scelta:

- **OBS Studio**: scene, sorgenti, uscite e audio su ogni PC di sala
- **NDI**: video e audio tra i PC, con un multiview di tutte le sale
- **Spectacast Meet, Mic e Translator**: la riunione come flussi separati, telefoni come microfoni, traduzione simultanea
- **Sennheiser EW-DX**: i radiomicrofoni della sala, con livello e batteria
- **MIDI e cartelle**: superfici di controllo e i video che vanno in onda durante l'evento
- **Dante**: l'audio in rete della sala, tramite Dante Virtual Soundcard su un PC
- **I tuoi**: qualsiasi apparecchio che parli HTTP, OSC o socket

Come collegare un tuo apparecchio, programmare le regole e usare l'API: [Fatto per essere esteso](/it/sviluppatori/).

## Fatto per la sala

Director gira su un PC in regia e parla con i PC di sala attraverso la rete della sede, così l'evento continua anche se cade internet. La pagina della flotta mostra a colpo d'occhio PC, riunione e uscita di ogni sala; i pannelli si compongono a blocchi, quindi una sala nuova è una copia in più, non un nuovo progetto. La dashboard parla italiano, inglese, tedesco e spagnolo.

{{shot:director-fleet|La flotta in Director: riunione, persone, sala d'attesa e uscita di ogni sala}}

{{plans:Director,Show,Complete}}

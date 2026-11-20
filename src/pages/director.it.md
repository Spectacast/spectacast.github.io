# Spectacast Director

<p class="lede">La regia per eventi ibridi dal vivo. Una sola dashboard vede insieme tutti i PC di sala, la riunione online e i microfoni, e le regole si occupano di quello che altrimenti qualcuno farebbe a mano, molte volte al giorno.</p>

{{cta}}

{{loop:director-speaker|Scegli una relatrice, apri il microfono, mettila in evidenza. Tre tocchi.|Registrazione dello schermo di Director: l'operatore sceglie la dott.ssa Elena Ortega nella Sala A, le apre il microfono e la mette in evidenza}}

## Tutte le sale su uno schermo

Ogni sala ha la sua colonna: chi è nella riunione e chi parla, la sala d'attesa e la lobby, Preview e Program, il banner e lo streaming. Scegli un relatore, lo mandi in onda con un tocco, e la sala successiva è subito accanto. Una sola persona può seguire un intero congresso; al congresso di 18 sale per cui Director è nato, è andata così.

{{closeup:director-hall|Primo piano della Sala A e della Sala B in Director: entrambe in onda, il PC di sala e tre persone in ogni riunione con il livello del microfono, e la sala d'attesa|**Rosso vuol dire in onda**, con la riunione e i microfoni.|**Chi è in riunione**, ognuno con il livello del microfono dal vivo.|**La sala d'attesa**: scegli chi aspetta, poi Ammetti.}}

## Regole per la routine

Ammettere la faculty appena arriva, tenere la sala d'attesa come è stata impostata, rimettere un video al suo posto quando un PC riparte, silenziare la sala mentre va un filmato: le regole reagiscono a quello che succede nella riunione, in OBS e sui microfoni, e lo fanno ogni volta allo stesso modo. Per ogni regola vedi quando è partita l'ultima volta e perché.

{{story:rule|Animazione: la dott.ssa Elena Ortega entra nella sala d'attesa della Sala A, la regola «Ammissione automatica» si accende e lei compare in riunione}}

{{loop:director-clip|Manda in onda un clip: il microfono della sala si silenzia da solo.|Registrazione dello schermo di Director: l'operatore mette il clip su Program nella Sala A, la sala passa a VOD e il suo microfono si silenzia; tornando alla riunione si riapre}}

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

## Fatto a modo tuo

Niente nella dashboard è fisso. I pannelli si compongono con blocchi nell'editor, le regole si compilano come Quando, Solo se e Allora, e un tuo apparecchio riceve un driver senza scrivere codice.

{{closeup:director-build-panel|Primo piano dell'editor dei pannelli di Director: la fila dei blocchi già pronti, la griglia del pannello con celle vuote e il pulsante Salva|**Blocchi**: una sala intera, una riunione o un monitor, costruiti una volta e messi dove servono.|**Fai clic su una cella vuota** per aggiungere un controllo o inserire un blocco, o su un controllo per modificarlo.|**Salva**, e il pannello è pronto all'uso.}}

{{closeup:director-build-rule|Primo piano dell'editor delle regole di Director con la regola «Active speaker → Speaker»: quando cambia chi parla in Zoom Sala A, dopo un tempo di attesa di 1500 ms, OBS Sala A imposta la sua scena|**Quando**: che cosa fa partire la regola. Qui cambia chi parla nella Sala A.|**Solo se**: una condizione e un tempo di attesa. Qui chi parla deve tenere la parola per un secondo e mezzo.|**Allora**: che cosa fa. Qui OBS della Sala A cambia scena.}}

## Fatto per la sala

Director gira su un PC in regia e parla con i PC di sala attraverso la rete della sede, così l'evento continua anche se cade internet. La pagina della flotta mostra a colpo d'occhio PC, riunione e uscita di ogni sala; i pannelli si compongono a blocchi, quindi una sala nuova è una copia in più, non un nuovo progetto. La dashboard parla italiano, inglese, tedesco e spagnolo.

{{closeup:director-fleet|Primo piano della pagina della flotta di Director: quattro sale, ognuna online e nella sua riunione, con i livelli dei microfoni e la sala d'attesa|**Il PC di ogni sala**: online e nella sua riunione.|**Chi parla**: una barra per microfono, dal vivo.|**La sala d'attesa**: da qui ammetti tutti, oppure la accendi e la spegni.}}

{{plans:Director,Show,Complete}}

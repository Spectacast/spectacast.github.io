# Fatto per essere esteso

<p class="lede">In ogni sede c'è un apparecchio che nessuno aveva previsto. Spectacast Director è fatto perché tu possa collegarlo da solo: descrivi il suo protocollo in un modulo, risolvi con uno script ciò che i moduli non sanno dire e comanda tutto dai tuoi sistemi con la sua API.</p>

{{cta}}

## Collega un apparecchio senza codice

Nella pagina Driver descrivi il protocollo di un dispositivo: i comandi che accetta e i messaggi che rimanda. Director parla OSC, UDP, TCP, HTTP e WebSocket, quanto basta per la maggior parte di console luci, mixer audio, mixer video e matrici. Una volta descritto, il dispositivo ha pulsanti, stato dal vivo e regole come quelli inclusi.

Lo provi sul dispositivo vero, con ogni messaggio in entrata e in uscita elencato dal vivo, e condividi un driver finito come un solo file.

[Come descrivere un driver →](/it/guida/director-drivers/)

{{closeup:director-build-driver|Primo piano dell'editor dei driver di Director con l'esempio «Generic OSC device»: il trasporto OSC su UDP, le impostazioni che ogni dispositivo richiede e i primi comandi|**Come parla**: OSC, UDP, TCP, HTTP o WebSocket.|**Che cosa serve a ogni dispositivo**: qui, due porte oltre al suo indirizzo.|**I suoi comandi**: ognuno diventa un'azione per pulsanti e regole.}}

## Regole, e script quando le regole non bastano

Le regole reagiscono a ciò che succede nelle sale: qualcuno entra in sala d'attesa, un relatore prende la parola, una sorgente va offline. Quasi tutte si costruiscono con dei moduli. Dove la logica è la tua, un passo può essere qualche riga di JavaScript con tutto lo stato a portata di mano.

{{closeup:director-build-rule|Primo piano dell'editor delle regole di Director con la regola «Active speaker → Speaker»: quando cambia chi parla in Zoom Sala A, dopo un tempo di attesa di 1500 ms, OBS Sala A imposta la sua scena|**Quando**: che cosa fa partire la regola. Qui cambia chi parla nella Sala A.|**Solo se**: una condizione e un tempo di attesa. Qui chi parla deve tenere la parola per un secondo e mezzo.|**Allora**: che cosa fa. Qui OBS della Sala A cambia scena.}}

[Regole e script →](/it/guida/director-rules/)

## Un'API per i tuoi sistemi

Tutto ciò che fa la dashboard passa da un'API HTTP sul PC di regia, e un WebSocket invia ogni cambiamento appena avviene. Un sistema di iscrizioni, un controller di show o uno script può leggere lo stato di ogni sala, premere un pulsante, impostare una variabile o eseguire una regola, ciascuno con un token che limita ciò che può fare.

[L'API →](/it/guida/director-api/)

## Webhook e ingresso OSC

Un altro sistema avvia qualcosa in Director con una sola chiamata: un webhook via HTTP o un messaggio OSC. Il programma del congresso può annunciare una sessione, e una regola mette il titolo giusto sulla sala giusta.

## Stream Deck e MIDI

Un tasto dello Stream Deck preme qualsiasi controllo della dashboard attraverso Bitfocus Companion, senza installare altro. Una superficie di controllo MIDI dà all'operatore fader e tasti veri, e le regole possono illuminarli.

## I tuoi pannelli

I pannelli della dashboard li disponi tu: pulsanti, selezioni, campi di testo, indicatori di livello e immagini dal vivo, costruiti una volta come blocco e collocati una volta per sala.

{{closeup:director-build-panel|Primo piano dell'editor dei pannelli di Director: la fila dei blocchi già pronti, la griglia del pannello con celle vuote e il pulsante Salva|**Blocchi**: una sala intera, una riunione o un monitor, costruiti una volta e messi dove servono.|**Fai clic su una cella vuota** per aggiungere un controllo o inserire un blocco, o su un controllo per modificarlo.|**Salva**, e il pannello è pronto all'uso.}}

[Pannelli →](/it/guida/director-panels/)

## Il tuo apparecchio non si può collegare così?

Alcuni apparecchi richiedono la libreria del loro produttore. Quei driver sono integrati in Director, come quelli per OBS Studio, NDI e Sennheiser EW-DX.

[Scrivici cosa vuoi controllare →](/it/contatti/)

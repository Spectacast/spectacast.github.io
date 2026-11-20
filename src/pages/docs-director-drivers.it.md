# Il tuo driver

<p class="lede">La pagina Driver descrive il protocollo di un dispositivo senza codice. Una volta descritto, il dispositivo ha azioni, eventi e stato come uno di quelli inclusi, e pannelli e regole lo usano allo stesso modo.</p>

Un driver definito da te parla uno di cinque trasporti: **OSC**, **UDP**, **TCP**, **HTTP** o **WebSocket**. Bastano per la maggior parte di console luci, mixer audio, mixer video, matrici e sistemi di controllo degli edifici.

## 1. Creare il driver

Nella pagina **Driver** fai clic su **+ driver su…** e scegli il trasporto. Dai un nome al driver ed elenca le impostazioni che ogni suo dispositivo richiede: un host, una porta, una chiave API. Un'impostazione ha un valore predefinito oppure è segnata con **obbl.** (obbligatoria), e i modelli qui sotto la leggono come `config.<id>`.

{{closeup:director-build-driver|Primo piano dell'editor dei driver di Director con l'esempio «Generic OSC device»: il trasporto OSC su UDP, le impostazioni che ogni dispositivo richiede e i primi comandi|**Come parla**: OSC, UDP, TCP, HTTP o WebSocket.|**Che cosa serve a ogni dispositivo**: qui, due porte oltre al suo indirizzo.|**I suoi comandi**: ognuno diventa un'azione per pulsanti e regole.}}

## 2. Comandi

Fai clic su **+ comando** per ogni cosa che si può dire al dispositivo. Un comando diventa un'azione che pulsanti e regole possono eseguire.

- I suoi **parametri** sono campi tipizzati, letti nel messaggio come `params.<id>`.
- Il suo **messaggio** è un modello. Per OSC è un indirizzo con argomenti tipizzati, come `/cue/{{params.cue}}/go`. Per HTTP è un metodo, un percorso, intestazioni e un corpo. Per UDP, TCP e WebSocket è una riga di testo, oppure byte scritti in esadecimale per un protocollo binario.

## 3. Feedback

Fai clic su **+ voce di feedback** per ogni messaggio che il dispositivo rimanda. Una voce riconosce un messaggio e dice cosa farne.

- **Riconoscere** con un modello di indirizzo OSC (`/cue/{n}/active`, dove `{n}` cattura una parte dell'indirizzo), con un'espressione regolare sul testo o con un'espressione su un messaggio JSON.
- **Impostare lo stato:** scrivere valori del messaggio nello stato del dispositivo, dove i pannelli li mostrano e le regole li leggono.
- **Generare un evento** a cui una regola può reagire.

Un driver HTTP può anche **interrogare**: chiama un indirizzo ogni pochi secondi e fa passare la risposta dalle stesse voci.

## 4. Online o offline

I dispositivi TCP e WebSocket sono online finché la connessione è attiva, e Director si ricollega da solo. I dispositivi UDP, OSC e HTTP hanno bisogno di un **heartbeat**: un comando inviato a intervalli la cui risposta mostra che il dispositivo c'è. Senza, risultano online.

## 5. Provarlo sul dispositivo vero

Fai clic su **Crea driver**, poi aggiungi un dispositivo con il tuo driver nella pagina **Dispositivi**. Tornato nella pagina **Driver**, fai clic su **prova** sulla scheda del driver, scegli il dispositivo e fai clic su **traccia i messaggi**. Ogni messaggio in entrata e in uscita viene elencato dal vivo, e ognuno di quelli in entrata mostra quali voci di feedback gli corrispondono e cosa imposterebbero. **Invia prova** esegue un comando con i parametri che scrivi.

## 6. Condividerlo

**esporta** scarica la definizione come file JSON; **importa JSON** ne aggiunge una a un altro show. Le definizioni sono salvate nel file dello show, quindi uno show porta con sé i suoi driver.

Due esempi da importare e adattare: [un dispositivo OSC generico](/examples/drivers/generic-osc.json) e [un dispositivo HTTP il cui stato viene interrogato a intervalli](/examples/drivers/http-example.json).

## Quando non basta

Un dispositivo che richiede la libreria del suo produttore, o un protocollo che questi cinque trasporti non possono portare, ha bisogno di un driver integrato in Director. [Scrivici](/it/contatti/) quale dispositivo vuoi controllare.

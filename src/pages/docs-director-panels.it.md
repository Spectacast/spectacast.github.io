# Pannelli

<p class="lede">Un pannello è una pagina di controlli che disponi tu: pulsanti, interruttori, selezioni, campi di testo e i riquadri di ogni sala. I pannelli dello show di esempio sono un punto di partenza, e ognuno si può modificare.</p>

{{shot:director-panels|Un pannello di Director con quattro sale: un blocco per sala, con la riunione, la sala d'attesa, Preview e Program}}

## Modificare un pannello

Nella pagina **Pannelli** fai clic su **Modifica**. Ora un clic su una cella vuota aggiunge un controllo, e un clic su un controllo ne apre le proprietà.

- Seleziona più controlli con Maiusc-clic o trascinando un rettangolo, poi spostali, copiali o eliminali insieme.
- **Annulla** e **Ripeti** tornano indietro e avanti fino a cento passi.
- **Salva** conserva le modifiche per ogni dashboard; **Scarta** le elimina.

**+ pannello** aggiunge una pagina. Chi accede con il PIN operatore vede i pannelli e nient'altro.

{{closeup:director-build-panel|Primo piano dell'editor dei pannelli di Director: la fila dei blocchi già pronti, la griglia del pannello con celle vuote e il pulsante Salva|**Blocchi**: una sala intera, una riunione o un monitor, costruiti una volta e messi dove servono.|**Fai clic su una cella vuota** per aggiungere un controllo o inserire un blocco, o su un controllo per modificarlo.|**Salva**, e il pannello è pronto all'uso.}}

## Controlli

| Controllo | Cosa fa |
|---|---|
| **Pulsante** | Esegue i suoi passi quando viene premuto |
| **Interruttore** | Un elenco di passi per accendere e uno per spegnere |
| **Selezione (opzioni)** | Una fila di opzioni: un elenco fisso o uno dal vivo, come le scene di un OBS o le persone in una riunione |
| **Campo di testo** | Un campo con un pulsante per applicare, per un sottopancia o un nome |
| **Etichetta** | Mostra un testo o un valore |
| **Stato del dispositivo** | Mostra se un dispositivo è collegato |
| **Anteprima (immagine di un dispositivo)** | L'immagine dal vivo di un OBS o di una sorgente NDI |
| **Mixer (ingressi audio di un dispositivo)** | Fader e mute per gli ingressi audio di un dispositivo |
| **Cornice (gruppo)** | Un bordo con titolo attorno ai controlli che vanno insieme |
| **Blocco** | Un insieme di controlli costruito una volta e collocato molte volte |

## Cosa fa una pressione

Una pressione esegue un elenco di passi, dall'alto:

- un'**azione** su un dispositivo, come «cambia la scena di programma»;
- un'**attesa**;
- l'**impostazione di una variabile**;
- un **se** con un elenco per il sì e uno per il no;
- passi eseguiti **in parallelo**, oppure una volta **per ogni** elemento di un elenco.

**Chiedi prima** fa porre una domanda alla dashboard prima di eseguire i passi: per i pulsanti che nessuno deve premere per sbaglio.

## Feedback: l'aspetto di un controllo

Le voci di **Feedback** cambiano colore e testo di un controllo in base allo stato dal vivo: rosso finché una sala è in onda, un nome quando qualcuno è in sala d'attesa. Le voci vengono provate dall'alto, e vince la prima che è vera.

## Blocchi: una striscia per ogni sala

Costruisci una volta i controlli di una sala, selezionali e fai clic su **Crea blocco**. I dispositivi che nominano diventano i **Valori** del blocco. Colloca il blocco una volta per sala e dai a ogni copia i suoi dispositivi. Una modifica al blocco arriva a tutte le sale insieme.

## Variabili

La pagina **Variabili** contiene i valori condivisi da pannelli e regole: il video scelto, il relatore che ha la parola. **Aggiungi variabile** ne crea una, con il suo tipo e il suo valore iniziale.

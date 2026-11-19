# Guida di Pass

<p class="lede">Configura un evento in Pass, trasforma i telefoni in lettori agli ingressi e ottieni le presenze a evento finito. Pass funziona nel browser, su spectacast.com/pass.</p>

## 1. L'evento

Accedi a [spectacast.com/pass](/pass/) con il tuo account Spectacast e crea un **Nuovo evento**. Poi, in **Configurazione**:

- **Zone:** le sale dove si conta la presenza.
- **Varchi:** uno per ingresso, ognuno in una zona.
- **Sessioni:** il programma. Segna con **Conta** le sessioni che contano per le presenze.
- **Categorie:** i tipi di partecipanti, come Faculty, iscritti o staff.

La lista in alto dice cosa manca ancora.

## 2. Partecipanti e badge

In **Partecipanti**:

- **+ Persona** aggiunge qualcuno a mano, ad esempio chi si iscrive al desk.
- **Importa** legge un CSV, o un Excel salvato come CSV, con intestazioni come Nome, Cognome, Email, Categoria e ID (vanno bene anche in inglese o tedesco). Le altre colonne restano come campi che regole e messaggi possono usare. Importando di nuovo si aggiornano le stesse persone.
- I **Feed** scaricano da soli l'elenco da un sito di iscrizione, e le **Chiavi per altri sistemi** permettono a un sito di inviare le sue iscrizioni. Chiedi al fornitore del tuo sito di iscrizione, o a noi, di collegarli.

Ogni partecipante riceve un badge con un codice QR. **Stampa tutti i badge** li stampa, sul tuo sfondo se ne carichi uno, oppure **Invia badge via email** manda a ognuno il suo.

## 3. Gli ingressi

A ogni ingresso usa un telefono o un tablet, oppure un lettore a tastiera collegato a un portatile.

1. In **Configurazione**, **Varchi**, premi **Configura un telefono** per quel varco.
2. Inquadra con la fotocamera del telefono il codice QR sullo schermo e apri il link. L'app del varco si apre su quel varco, senza scrivere nulla.
3. Aggiungila alla schermata Home, così si apre come un'app.

Il varco risponde a ogni badge all'istante, a tutto schermo in verde, giallo o rosso, con un suono e il nome della persona. Se cade la rete, il varco continua a decidere da solo e invia le sue scansioni quando la rete torna.

{{phone:pass-door-welcome|L'app dell'ingresso su un telefono: uno schermo verde con «Welcome Sofia»}}

Un **lettore a tastiera** funziona sulla stessa pagina del varco: impostalo perché invii Invio dopo ogni codice. Un lettore in modalità memoria, a un varco senza schermo, si scarica dopo in **Carica scansioni**.

## 4. Regole

Cosa dice un varco lo decidono le **Regole**, provate dall'alto; la prima che corrisponde decide. Un evento nuovo parte con regole sensate: ignorare una doppia lettura, respingere badge sconosciuti o annullati, avvisare quando qualcuno è già dentro, respingere una sala piena, dare il benvenuto a tutti gli altri. Aggiungi le tue, ad esempio una sala riservata a una categoria, e prova qualsiasi badge con **Prova una scansione** prima di aprire le porte.

## 5. Durante l'evento

**In diretta** mostra quante persone ci sono in ogni sala, le ultime scansioni, i telefoni ai varchi e se sono online. Ciò che un varco ha deciso offline diversamente dal server compare in **Da controllare**.

## 6. Dopo

I **Report** danno, per persona, i minuti e la percentuale in ogni sessione, pronti per Excel. In **Attestati** stabilisci cosa serve per un attestato di partecipazione; chi lo soddisfa scarica il suo.

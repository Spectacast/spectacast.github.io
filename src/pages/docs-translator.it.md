# Guida di Translator

<p class="lede">Translator ascolta chi parla e dice ciò che dice in un'altra lingua, dal vivo, su qualsiasi uscita audio. Un Translator, detto corsia, per lingua.</p>

## Cosa ti serve

- Un PC Windows in sala o in regia, installato con Spectacast Setup e attivato nel tuo account.
- Un piano con Translator: i suoi minuti arrivano con la licenza del PC, senza configurare nulla. Oppure una tua chiave Google Gemini o OpenAI.
- Un ingresso con la voce di chi parla: un microfono, il mixer, un telefono tramite [Mic](/it/guida/mic/) o un segnale via NDI.

## La pagina di controllo

Ogni corsia ha la sua pagina di controllo, su **http://127.0.0.1:4720** per la prima corsia di quel PC. Scegli:

1. l'**ingresso**: una scheda audio, o una sorgente NDI come un partecipante di [Meet](/it/guida/meet/);
2. l'**uscita**: una scheda audio, un cavo virtuale verso OBS o il mixer, o il canale di interpretariato di Meet;
3. la **lingua** in cui parlare;

e premi **Avvia**. La pagina mostra ogni frase due volte, come sentita e come detta, mentre viene pronunciata.

{{shot:translator|La pagina di controllo di Translator: quello che è stato sentito in italiano e quello che è stato detto in inglese, riga per riga}}

## Motori

Il motore decide come suona Translator e quanto velocemente risponde. Google Gemini è quello predefinito; OpenAI è l'altro. I motori **interprete** lavorano come un'interprete di congresso: dai loro l'**Argomento** della sessione e un glossario di nomi e termini tecnici, uno per riga, e li usano.

## Senso capovolto

Mentre una corsia lavora, un secondo modello legge ciò che è stato sentito accanto a ciò che è stato detto e segna in rosso i punti in cui la traduzione dice altro: un «non» perso, un numero, sinistra per destra, un nome. Non cambia nulla di ciò che dice la corsia; serve a chi la segue. La casella **Avvisa quando il senso si capovolge** lo spegne.

## Nella riunione

Per dare una lingua a chi ascolta nella riunione online, imposta l'uscita della corsia sul canale di interpretariato di Meet. Meet entra come interprete di quella lingua, e chi ascolta sceglie la lingua in Zoom. Vedi [Meet](/it/guida/meet/).

## Dopo un riavvio

Una corsia ricorda cosa stava facendo. Dopo un riavvio del PC torna con lo stesso ingresso, la stessa uscita e la stessa lingua, e riparte se era avviata; riprova per dieci minuti finché manca una scheda audio o la rete.

## Minuti

Ogni minuto in cui una corsia parla conta, per lingua. I piani con Translator includono {{INCLUDED_MINUTES}} minuti per sala; il tuo account mostra quanti ne hai usati. Vedi [Account e fatturazione](/it/guida/account-e-fatturazione/).

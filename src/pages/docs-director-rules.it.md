# Regole e script

<p class="lede">Una regola fa ciò che altrimenti farebbe un operatore a mano: quando succede qualcosa e una condizione è vera, esegue un elenco di passi. Sono le regole a permettere a un solo operatore di seguire molte sale.</p>

## Una regola ha tre parti

1. **Trigger:** un evento di un dispositivo (qualcuno entra in sala d'attesa), un valore dello stato che cambia (un OBS inizia a trasmettere), un intervallo oppure **Solo se avviata a mano**. Un trigger può osservare un dispositivo o tutti i dispositivi di un driver, così una regola serve tutte le sale.
2. **Condizione** (facoltativa): un'espressione che deve essere vera, come `obs.studioA.streaming`.
3. **Passi:** gli stessi passi che esegue un pulsante. Vedi [Pannelli](/it/guida/director-panels/).

Nella pagina **Regole**, **+ regola** inizia una regola vuota e **+ da modello** ne costruisce una comune con i tuoi dispositivi, per esempio «chi parla va su una scena dopo un tempo di attesa» o «una sorgente NDI va offline, passa a una scena di riserva».

{{shot:director-rules|Le regole di Director: ognuna con ciò che la fa partire e la sua ultima esecuzione}}

## Tempi e ordine

- **tempo di attesa (ms):** la regola aspetta, e conta solo l'ultimo trigger di una raffica. Chi parla deve tenere la parola per un momento prima che l'immagine cambi.
- **pausa minima (ms):** la regola non riparte per questo tempo.
- **priorità:** quando un evento corrisponde a più regole, parte prima la più alta.

## Provare prima di fidarsi

- **simulazione:** la regola annota ciò che farebbe e non fa nulla.
- **Esegui ora** esegue una regola una volta senza aspettare il suo trigger. La sua condizione deve comunque essere vera.
- **Cronologia**, in fondo alla pagina, elenca ogni esecuzione e ogni salto con il motivo, e ogni azione con il suo errore.
- **Diagramma** disegna tutte le regole: i trigger a sinistra, le regole al centro e, a destra, i dispositivi su cui agiscono.

L'interruttore **AUTOMAZIONE ACCESA**, in alto nella pagina **Regole**, mette in pausa tutte le regole insieme. Finché sono in pausa mostra **AUTOMAZIONE SPENTA**, e l'intestazione mostra lo stesso in ogni pagina. I pulsanti ed **Esegui ora** continuano a funzionare.

## Passi di script

Per la logica che i moduli non sanno esprimere, un passo può essere un breve frammento di JavaScript. Gira sul PC di regia e ha a portata di mano ciò che gli serve:

| Nome | Cos'è |
|---|---|
| `state` | Tutto ciò che Director sa di ogni dispositivo |
| `event` | Ciò che ha avviato la regola |
| `vars` | Le variabili |
| `setVar(id, value)` | Imposta una variabile |
| `await run(target, action, params)` | Esegue un'azione su un dispositivo |
| `log(...)` | Scrive una riga nel registro degli eventi |
| `await sleep(ms)` | Aspetta |

```
// Trigger: l'evento "Entered the waiting room" di una riunione.
// Ammettere subito i relatori; tutti gli altri aspettano l'operatore.
if (event.name.startsWith('Dr.')) {
  await run({ eventDevice: true }, 'admit', { by: 'zoomID', user: event.zoomId });
  log('admitted', event.name);
}
```

**Prova (simulazione)** nell'editor esegue il frammento una volta senza toccare alcun dispositivo e ne mostra il registro. Un frammento che fallisce, o che dura più del suo **timeout (ms)** (cinque secondi se non lo cambi), conta come un passo fallito, e i passi successivi vengono eseguiti lo stesso.

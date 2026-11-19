# API, webhook e Stream Deck

<p class="lede">Tutto ciò che fa la dashboard passa da un'API HTTP sul PC di regia, e anche altri programmi possono usarla: un sistema di iscrizioni, un controller di show, uno script, uno Stream Deck.</p>

Sul PC di regia l'indirizzo è `http://127.0.0.1:4700`. Un altro computer raggiunge `http://<PC di regia>:4700` quando `.env` contiene `HOST=0.0.0.0` e un `PIN` (vedi la [guida di Director](/it/guida/director/)). L'API è HTTP non cifrato e resta sulla rete della sede: Director non la apre a internet.

## Accesso

I token di accesso funzionano solo se è impostato un PIN. Per un programma, aggiungi un token di accesso suo in `C:\ProgramData\Spectacast\director\.env`, poi esci e rientra in Windows:

```
ACCESS_TOKENS=api:<un token di almeno 8 caratteri>
```

| Token | Cosa può fare |
|---|---|
| `api:<token>` | Leggere tutto, premere i controlli, impostare variabili, eseguire regole, chiamare i webhook. Non può modificare lo show |
| `viewer:<token>` | Solo leggere |
| `operator:<token>` | Come il PIN operatore: i pannelli |
| `panels:<token>` | Solo i pannelli, per uno schermo in una sala |

Un programma accede con `POST /api/login` e il corpo `{ "pin": "<token>" }`, e conserva il cookie di sessione che riceve. Una sessione finisce quando Director si riavvia: accedi di nuovo quando una chiamata risponde `401`. Cinque tentativi sbagliati bloccano un indirizzo per 30 secondi. I webhook portano il token a ogni chiamata; le richieste dello Stream Deck portano il PIN o il PIN operatore.

## Cosa puoi chiamare

| Chiamata | Cosa fa |
|---|---|
| `GET /api/state` | Tutto ciò che Director sa, come un albero JSON |
| `GET /api/devices` | I dispositivi e se sono collegati |
| `GET /api/drivers` | Le azioni e gli eventi di ogni driver, come JSON Schema |
| `POST /api/actions` | Esegue un'azione: `{ "target": { "device": "obs01" }, "action": "setCurrentScene", "params": { … } }` |
| `POST /api/press` | Preme un controllo di un pannello: `{ "panel": "main", "control": "goLive" }` |
| `POST /api/vars` | Imposta una variabile: `{ "id": "segment", "value": "panel" }` |
| `POST /api/rules/<id>/run` | Esegue subito una regola |
| `GET /api/rules/history` | Le esecuzioni e i salti di ogni regola |
| `GET /ws` | Un WebSocket: tutto lo stato una volta, poi ogni cambiamento appena avviene |

Una pressione fatta dall'API o da uno Stream Deck viene eseguita subito: **Chiedi prima** chiede solo sulla dashboard.

## Webhook

Una chiamata a `POST /api/hooks/<name>` genera un evento a cui reagisce una regola. Il corpo JSON e i parametri dell'indirizzo diventano i campi dell'evento.

```
curl -X POST http://director:4700/api/hooks/session-start \
  -H "x-token: <token>" -H "content-type: application/json" \
  -d '{ "hall": "A", "title": "Opening" }'
```

Una regola con il trigger **webhook** e l'evento `session_start` legge poi `event.hall` ed `event.title`. Il token va in un'intestazione `x-token`, in `Authorization: Bearer` oppure nell'indirizzo come `?token=`.

L'operatore può trattenere i webhook con l'interruttore **LE CHIAMATE API SI APPLICANO** nella pagina **Regole**. Finché mostra **CHIAMATE API SOLO REGISTRATE**, una chiamata viene registrata e riceve `"applied": false`, e nessuna regola parte.

## Stream Deck

Bitfocus Companion raggiunge Director con il suo modulo **Generic HTTP**; in Companion non c'è nulla da installare. Un tasto invia una richiesta:

| Richiesta | Cosa fa |
|---|---|
| `/api/bridge/press/<panel>/<control>?token=<PIN>` | Preme un controllo, proprio come un tocco sulla dashboard |
| `/api/bridge/var/<id>?value=…&token=<PIN>` | Imposta una variabile |
| `/api/bridge/action/<device>/<action>?…&token=<PIN>` | Esegue l'azione di un dispositivo |
| `/api/bridge/rule/<id>/run?token=<PIN>` | Esegue una regola |

`<PIN>` è il PIN o, meglio, il PIN operatore (`OPERATOR_PIN`), che non può modificare lo show. Un token di accesso qui non funziona. L'id di un controllo è in alto nelle sue proprietà, nella pagina **Pannelli**.

Per i tasti che si illuminano in base allo stato, Director parla anche OSC con Companion: metti in `.env` `BRIDGE_OSC_PORT=<una porta UDP libera>` e `BRIDGE_OSC_FEEDBACK=<indirizzo di Companion>:<la sua porta di ascolto OSC>`, e fai inviare a Companion il messaggio OSC `/subscribe` con la parte dello stato che gli serve come argomento, per esempio `obs.obs01`. La porta OSC non chiede PIN: usala solo sulla rete di regia.

## MIDI

Una superficie di controllo è un dispositivo come gli altri: aggiungila nella pagina **Dispositivi** con il driver **MIDI controller**. I suoi tasti e fader arrivano come eventi per le regole, e le regole possono illuminarne i tasti.

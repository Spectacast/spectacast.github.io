# API, webhook e Stream Deck

<p class="lede">Tutto ciò che fa la dashboard passa da un'API HTTP sul PC di regia, e anche altri programmi possono usarla: un sistema di iscrizioni, un controller di show, uno script, uno Stream Deck.</p>

L'indirizzo è quello della dashboard, di norma `http://<PC di regia>:4700`. L'API resta sulla rete della sede: Director non la apre a internet.

## Accesso

Imposta un PIN prima di aprire Director alla rete (vedi la [guida di Director](/it/guida/director/)). Per un programma, aggiungi un token di accesso suo in `C:\ProgramData\Spectacast\director\.env`, poi esci dalla sessione e rientra:

```
ACCESS_TOKENS=api:<un token di almeno 8 caratteri>
```

| Token | Cosa può fare |
|---|---|
| `api:<token>` | Leggere tutto, premere i controlli, impostare variabili, eseguire regole, chiamare i webhook. Non può modificare lo show |
| `viewer:<token>` | Solo leggere |
| `operator:<token>` | Come il PIN operatore: i pannelli |
| `panels:<token>` | Solo i pannelli, per uno schermo in una sala |

Un programma accede con `POST /api/login` e il corpo `{ "pin": "<token>" }`, e conserva il cookie di sessione che riceve. Le chiamate dei webhook e dello Stream Deck portano il token con sé, come mostrato sotto.

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

## Webhook

Una chiamata a `POST /api/hooks/<name>` genera un evento a cui reagisce una regola. Il corpo JSON e i parametri dell'indirizzo diventano i campi dell'evento.

```
curl -X POST http://director:4700/api/hooks/session-start \
  -H "x-token: <token>" -H "content-type: application/json" \
  -d '{ "hall": "A", "title": "Opening" }'
```

Una regola con il trigger **webhook** e l'evento `session_start` legge poi `event.hall` ed `event.title`. Il token va in un'intestazione `x-token`, in `Authorization: Bearer` oppure nell'indirizzo come `?token=`.

## Stream Deck

Bitfocus Companion raggiunge Director con il suo modulo **Generic HTTP**; in Companion non c'è nulla da installare. Un tasto invia una richiesta:

| Richiesta | Cosa fa |
|---|---|
| `/api/bridge/press/<panel>/<control>?token=<PIN>` | Preme un controllo, proprio come un tocco sulla dashboard |
| `/api/bridge/var/<id>?value=…&token=<PIN>` | Imposta una variabile |
| `/api/bridge/action/<device>/<action>?…&token=<PIN>` | Esegue l'azione di un dispositivo |
| `/api/bridge/rule/<id>/run?token=<PIN>` | Esegue una regola |

L'id di un controllo è in alto nelle sue proprietà, nella pagina **Pannelli**. Per i tasti che si illuminano in base allo stato, Director parla anche OSC con Companion: metti `BRIDGE_OSC_PORT=<una porta UDP libera>` in `.env`.

## MIDI

Una superficie di controllo è un dispositivo come gli altri: aggiungila nella pagina **Dispositivi** con il driver **MIDI controller**. I suoi tasti e fader arrivano come eventi per le regole, e le regole possono illuminarne i tasti.

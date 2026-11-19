# API, webhooks and Stream Deck

<p class="lede">Everything the dashboard does goes through an HTTP API on the control-room PC, and other programs can use it too: a registration system, a show controller, a script, a Stream Deck.</p>

The address is that of the dashboard, by default `http://<control-room PC>:4700`. The API stays on the venue's network: Director does not open it to the internet.

## Access

Set a PIN before you open Director to the network (see the [Director guide](/docs/director/)). For a program, add an access token of its own to `C:\ProgramData\Spectacast\director\.env`, then log off and on again:

```
ACCESS_TOKENS=api:<a token of 8 characters or more>
```

| Token | What it may do |
|---|---|
| `api:<token>` | Read everything, press controls, set variables, run rules, call webhooks. It cannot change the show |
| `viewer:<token>` | Read only |
| `operator:<token>` | The same as the operator PIN: the panels |
| `panels:<token>` | The panels alone, for a screen in a hall |

A program signs in with `POST /api/login` and the body `{ "pin": "<token>" }`, and keeps the session cookie it gets back. Webhooks and Stream Deck calls carry the token themselves, as shown below.

## What you can call

| Call | What it does |
|---|---|
| `GET /api/state` | Everything Director knows, as one JSON tree |
| `GET /api/devices` | The devices and whether they are connected |
| `GET /api/drivers` | Every driver's actions and events, as JSON Schema |
| `POST /api/actions` | Runs an action: `{ "target": { "device": "obs01" }, "action": "setCurrentScene", "params": { … } }` |
| `POST /api/press` | Presses a panel control: `{ "panel": "main", "control": "goLive" }` |
| `POST /api/vars` | Sets a variable: `{ "id": "segment", "value": "panel" }` |
| `POST /api/rules/<id>/run` | Runs a rule now |
| `GET /api/rules/history` | The runs and skips of every rule |
| `GET /ws` | A WebSocket: the whole state once, then every change as it happens |

## Webhooks

A call to `POST /api/hooks/<name>` raises an event that a rule reacts to. The JSON body and the query string become the event's fields.

```
curl -X POST http://director:4700/api/hooks/session-start \
  -H "x-token: <token>" -H "content-type: application/json" \
  -d '{ "hall": "A", "title": "Opening" }'
```

A rule with the trigger **webhook**, event `session_start`, then reads `event.hall` and `event.title`. The token goes in an `x-token` header, in `Authorization: Bearer`, or in the address as `?token=`.

## Stream Deck

Bitfocus Companion reaches Director with its **Generic HTTP** module; there is nothing to install in Companion. A key sends one request:

| Request | What it does |
|---|---|
| `/api/bridge/press/<panel>/<control>?token=<PIN>` | Presses a control, exactly like a tap on the dashboard |
| `/api/bridge/var/<id>?value=…&token=<PIN>` | Sets a variable |
| `/api/bridge/action/<device>/<action>?…&token=<PIN>` | Runs a device's action |
| `/api/bridge/rule/<id>/run?token=<PIN>` | Runs a rule |

The control's id is at the top of its properties on the **Panels** page. For keys that light up with the state, Director also speaks OSC to Companion: set `BRIDGE_OSC_PORT=<a free UDP port>` in `.env`.

## MIDI

A control surface is a device like any other: add it on the **Devices** page with the **MIDI controller** driver. Its keys and faders arrive as events for rules, and rules can light its keys.

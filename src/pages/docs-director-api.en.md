# API, webhooks and Stream Deck

<p class="lede">Everything the dashboard does goes through an HTTP API on the control-room PC, and other programs can use it too: a registration system, a show controller, a script, a Stream Deck.</p>

On the control-room PC the address is `http://127.0.0.1:4700`. Another machine reaches `http://<control-room PC>:4700` once `.env` has `HOST=0.0.0.0` and a `PIN` (see the [Director guide](/docs/director/)). The API is plain HTTP and stays on the venue's network: Director does not open it to the internet.

## Access

Access tokens work only when a PIN is set. For a program, add an access token of its own to `C:\ProgramData\Spectacast\director\.env`, then log off and on again:

```
ACCESS_TOKENS=api:<a token of 8 characters or more>
```

| Token | What it may do |
|---|---|
| `api:<token>` | Read everything, press controls, set variables, run rules, call webhooks. It cannot change the show |
| `viewer:<token>` | Read only |
| `operator:<token>` | The same as the operator PIN: the panels |
| `panels:<token>` | The panels alone, for a screen in a hall |

A program signs in with `POST /api/login` and the body `{ "pin": "<token>" }`, and keeps the session cookie it gets back. A session ends when Director restarts: sign in again when a call answers `401`. Five wrong tries lock an address out for 30 seconds. Webhooks carry the token with every call; Stream Deck requests carry the PIN or the operator PIN.

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

A press through the API or from a Stream Deck runs at once: **Ask first** asks on the dashboard only.

## Webhooks

A call to `POST /api/hooks/<name>` raises an event that a rule reacts to. The JSON body and the query string become the event's fields.

```
curl -X POST http://director:4700/api/hooks/session-start \
  -H "x-token: <token>" -H "content-type: application/json" \
  -d '{ "hall": "A", "title": "Opening" }'
```

A rule with the trigger **webhook**, event `session_start`, then reads `event.hall` and `event.title`. The token goes in an `x-token` header, in `Authorization: Bearer`, or in the address as `?token=`.

The operator can hold webhooks back with the **API CALLS APPLY** switch on the **Rules** page. While it reads **API CALLS ONLY LOGGED**, a call is logged and answered with `"applied": false`, and no rule runs.

## Stream Deck

Bitfocus Companion reaches Director with its **Generic HTTP** module; there is nothing to install in Companion. A key sends one request:

| Request | What it does |
|---|---|
| `/api/bridge/press/<panel>/<control>?token=<PIN>` | Presses a control, exactly like a tap on the dashboard |
| `/api/bridge/var/<id>?value=…&token=<PIN>` | Sets a variable |
| `/api/bridge/action/<device>/<action>?…&token=<PIN>` | Runs a device's action |
| `/api/bridge/rule/<id>/run?token=<PIN>` | Runs a rule |

`<PIN>` is the PIN or, better, the operator PIN (`OPERATOR_PIN`), which cannot change the show. An access token does not work here. The control's id is at the top of its properties on the **Panels** page.

For keys that light up with the state, Director also speaks OSC to Companion: in `.env` set `BRIDGE_OSC_PORT=<a free UDP port>` and `BRIDGE_OSC_FEEDBACK=<Companion's address>:<its OSC listen port>`, and have Companion send the OSC message `/subscribe` with the part of the state it wants as its argument, such as `obs.obs01`. The OSC port asks for no PIN, so use it on the control-room network only.

## MIDI

A control surface is a device like any other: add it on the **Devices** page with the **MIDI controller** driver. Its keys and faders arrive as events for rules, and rules can light its keys.

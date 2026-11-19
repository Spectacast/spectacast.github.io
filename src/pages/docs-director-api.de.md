# API, Webhooks und Stream Deck

<p class="lede">Alles, was das Dashboard tut, läuft über eine HTTP-API auf dem Regie-PC, und andere Programme können sie ebenfalls nutzen: ein Registrierungssystem, eine Showsteuerung, ein Skript, ein Stream Deck.</p>

Die Adresse ist die des Dashboards, standardmäßig `http://<Regie-PC>:4700`. Die API bleibt im Netzwerk des Veranstaltungsorts: Director öffnet sie nicht zum Internet.

## Zugriff

Legen Sie eine PIN fest, bevor Sie Director im Netzwerk erreichbar machen (siehe die [Director-Anleitung](/de/hilfe/director/)). Für ein Programm tragen Sie ein eigenes Zugriffstoken in `C:\ProgramData\Spectacast\director\.env` ein und melden sich dann ab und wieder an:

```
ACCESS_TOKENS=api:<ein Token mit mindestens 8 Zeichen>
```

| Token | Was es darf |
|---|---|
| `api:<token>` | Alles lesen, Bedienelemente drücken, Variablen setzen, Regeln ausführen, Webhooks aufrufen. Die Show ändern kann es nicht |
| `viewer:<token>` | Nur lesen |
| `operator:<token>` | Dasselbe wie die Operator-PIN: die Panels |
| `panels:<token>` | Nur die Panels, für einen Bildschirm in einem Saal |

Ein Programm meldet sich mit `POST /api/login` und dem Body `{ "pin": "<token>" }` an und behält das Sitzungs-Cookie, das es zurückbekommt. Aufrufe von Webhooks und vom Stream Deck tragen das Token selbst, wie unten gezeigt.

## Was Sie aufrufen können

| Aufruf | Was er tut |
|---|---|
| `GET /api/state` | Alles, was Director weiß, als ein JSON-Baum |
| `GET /api/devices` | Die Geräte und ob sie verbunden sind |
| `GET /api/drivers` | Aktionen und Ereignisse jedes Treibers, als JSON Schema |
| `POST /api/actions` | Führt eine Aktion aus: `{ "target": { "device": "obs01" }, "action": "setCurrentScene", "params": { … } }` |
| `POST /api/press` | Drückt ein Bedienelement eines Panels: `{ "panel": "main", "control": "goLive" }` |
| `POST /api/vars` | Setzt eine Variable: `{ "id": "segment", "value": "panel" }` |
| `POST /api/rules/<id>/run` | Führt eine Regel jetzt aus |
| `GET /api/rules/history` | Läufe und Auslassungen jeder Regel |
| `GET /ws` | Ein WebSocket: einmal der ganze Zustand, dann jede Änderung, sobald sie geschieht |

## Webhooks

Ein Aufruf von `POST /api/hooks/<name>` löst ein Ereignis aus, auf das eine Regel reagiert. Der JSON-Body und die Parameter der Adresse werden zu den Feldern des Ereignisses.

```
curl -X POST http://director:4700/api/hooks/session-start \
  -H "x-token: <token>" -H "content-type: application/json" \
  -d '{ "hall": "A", "title": "Opening" }'
```

Eine Regel mit dem Auslöser **Webhook** und dem Ereignis `session_start` liest dann `event.hall` und `event.title`. Das Token steht in einem Header `x-token`, in `Authorization: Bearer` oder in der Adresse als `?token=`.

## Stream Deck

Bitfocus Companion erreicht Director mit seinem Modul **Generic HTTP**; in Companion ist nichts zu installieren. Eine Taste sendet eine Anfrage:

| Anfrage | Was sie tut |
|---|---|
| `/api/bridge/press/<panel>/<control>?token=<PIN>` | Drückt ein Bedienelement, genau wie ein Tippen im Dashboard |
| `/api/bridge/var/<id>?value=…&token=<PIN>` | Setzt eine Variable |
| `/api/bridge/action/<device>/<action>?…&token=<PIN>` | Führt die Aktion eines Geräts aus |
| `/api/bridge/rule/<id>/run?token=<PIN>` | Führt eine Regel aus |

Die ID eines Bedienelements steht oben in seinen Eigenschaften auf der Seite **Panels**. Für Tasten, die je nach Zustand leuchten, spricht Director mit Companion auch OSC: Tragen Sie `BRIDGE_OSC_PORT=<ein freier UDP-Port>` in `.env` ein.

## MIDI

Ein Bedienpult ist ein Gerät wie jedes andere: Fügen Sie es auf der Seite **Geräte** mit dem Treiber **MIDI controller** hinzu. Seine Tasten und Fader kommen als Ereignisse für Regeln an, und Regeln können seine Tasten leuchten lassen.

# API, webhooks y Stream Deck

<p class="lede">Todo lo que hace el dashboard pasa por una API HTTP en el PC de control, y otros programas también pueden usarla: un sistema de inscripciones, un controlador de show, un script, un Stream Deck.</p>

La dirección es la del dashboard, por defecto `http://<PC de control>:4700`. La API se queda en la red del recinto: Director no la abre a internet.

## Acceso

Fija un PIN antes de abrir Director a la red (consulta la [guía de Director](/es/ayuda/director/)). Para un programa, añade un token de acceso propio en `C:\ProgramData\Spectacast\director\.env` y después cierra la sesión y vuelve a iniciarla:

```
ACCESS_TOKENS=api:<un token de 8 caracteres o más>
```

| Token | Qué puede hacer |
|---|---|
| `api:<token>` | Leerlo todo, pulsar controles, fijar variables, ejecutar reglas, llamar a webhooks. No puede cambiar el show |
| `viewer:<token>` | Solo leer |
| `operator:<token>` | Lo mismo que el PIN de operador: los paneles |
| `panels:<token>` | Solo los paneles, para una pantalla en una sala |

Un programa inicia sesión con `POST /api/login` y el cuerpo `{ "pin": "<token>" }`, y conserva la cookie de sesión que recibe. Las llamadas de webhooks y de Stream Deck llevan el token ellas mismas, como se muestra abajo.

## Qué puedes llamar

| Llamada | Qué hace |
|---|---|
| `GET /api/state` | Todo lo que Director sabe, como un árbol JSON |
| `GET /api/devices` | Los dispositivos y si están conectados |
| `GET /api/drivers` | Las acciones y los eventos de cada driver, como JSON Schema |
| `POST /api/actions` | Ejecuta una acción: `{ "target": { "device": "obs01" }, "action": "setCurrentScene", "params": { … } }` |
| `POST /api/press` | Pulsa un control de un panel: `{ "panel": "main", "control": "goLive" }` |
| `POST /api/vars` | Fija una variable: `{ "id": "segment", "value": "panel" }` |
| `POST /api/rules/<id>/run` | Ejecuta una regla ahora |
| `GET /api/rules/history` | Las ejecuciones y omisiones de cada regla |
| `GET /ws` | Un WebSocket: todo el estado una vez, y después cada cambio en cuanto ocurre |

## Webhooks

Una llamada a `POST /api/hooks/<name>` lanza un evento al que reacciona una regla. El cuerpo JSON y los parámetros de la dirección pasan a ser los campos del evento.

```
curl -X POST http://director:4700/api/hooks/session-start \
  -H "x-token: <token>" -H "content-type: application/json" \
  -d '{ "hall": "A", "title": "Opening" }'
```

Una regla con el disparador **webhook** y el evento `session_start` lee entonces `event.hall` y `event.title`. El token va en una cabecera `x-token`, en `Authorization: Bearer` o en la dirección como `?token=`.

## Stream Deck

Bitfocus Companion llega a Director con su módulo **Generic HTTP**; no hay nada que instalar en Companion. Una tecla envía una petición:

| Petición | Qué hace |
|---|---|
| `/api/bridge/press/<panel>/<control>?token=<PIN>` | Pulsa un control, igual que un toque en el dashboard |
| `/api/bridge/var/<id>?value=…&token=<PIN>` | Fija una variable |
| `/api/bridge/action/<device>/<action>?…&token=<PIN>` | Ejecuta la acción de un dispositivo |
| `/api/bridge/rule/<id>/run?token=<PIN>` | Ejecuta una regla |

El id de un control está arriba en sus propiedades, en la página **Paneles**. Para las teclas que se iluminan según el estado, Director también habla OSC con Companion: pon `BRIDGE_OSC_PORT=<un puerto UDP libre>` en `.env`.

## MIDI

Una superficie de control es un dispositivo como cualquier otro: añádela en la página **Dispositivos** con el driver **MIDI controller**. Sus teclas y faders llegan como eventos para las reglas, y las reglas pueden iluminar sus teclas.

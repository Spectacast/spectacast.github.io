# API, webhooks y Stream Deck

<p class="lede">Todo lo que hace el dashboard pasa por una API HTTP en el PC de control, y otros programas también pueden usarla: un sistema de inscripciones, un controlador de show, un script, un Stream Deck.</p>

En el PC de control la dirección es `http://127.0.0.1:4700`. Otro equipo llega a `http://<PC de control>:4700` cuando `.env` tiene `HOST=0.0.0.0` y un `PIN` (consulta la [guía de Director](/es/ayuda/director/)). La API es HTTP sin cifrar y se queda en la red del recinto: Director no la abre a internet.

## Acceso

Los tokens de acceso solo funcionan si hay un PIN. Para un programa, añade un token de acceso propio en `C:\ProgramData\Spectacast\director\.env` y luego cierra la sesión y vuelve a entrar:

```
ACCESS_TOKENS=api:<un token de 8 caracteres o más>
```

| Token | Qué puede hacer |
|---|---|
| `api:<token>` | Leerlo todo, pulsar controles, fijar variables, ejecutar reglas, llamar a webhooks. No puede cambiar el show |
| `viewer:<token>` | Solo leer |
| `operator:<token>` | Lo mismo que el PIN de operador: los paneles |
| `panels:<token>` | Solo los paneles, para una pantalla en una sala |

Un programa inicia sesión con `POST /api/login` y el cuerpo `{ "pin": "<token>" }`, y conserva la cookie de sesión que recibe. Una sesión termina cuando Director se reinicia: inicia sesión de nuevo cuando una llamada responda `401`. Cinco intentos fallidos bloquean una dirección durante 30 segundos. Los webhooks llevan el token en cada llamada; las peticiones de Stream Deck llevan el PIN o el PIN de operador.

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

Una pulsación hecha por la API o desde un Stream Deck se ejecuta al momento: **Preguntar antes** solo pregunta en el dashboard.

## Webhooks

Una llamada a `POST /api/hooks/<name>` lanza un evento al que reacciona una regla. El cuerpo JSON y los parámetros de la dirección pasan a ser los campos del evento.

```
curl -X POST http://director:4700/api/hooks/session-start \
  -H "x-token: <token>" -H "content-type: application/json" \
  -d '{ "hall": "A", "title": "Opening" }'
```

Una regla con el disparador **webhook** y el evento `session_start` lee entonces `event.hall` y `event.title`. El token va en una cabecera `x-token`, en `Authorization: Bearer` o en la dirección como `?token=`.

El operador puede retener los webhooks con el interruptor **LAS LLAMADAS A LA API SE APLICAN** de la página **Reglas**. Mientras muestra **LLAMADAS A LA API SOLO REGISTRADAS**, una llamada se registra y recibe `"applied": false`, y no se ejecuta ninguna regla.

## Stream Deck

Bitfocus Companion llega a Director con su módulo **Generic HTTP**; no hay nada que instalar en Companion. Una tecla envía una petición:

| Petición | Qué hace |
|---|---|
| `/api/bridge/press/<panel>/<control>?token=<PIN>` | Pulsa un control, igual que un toque en el dashboard |
| `/api/bridge/var/<id>?value=…&token=<PIN>` | Fija una variable |
| `/api/bridge/action/<device>/<action>?…&token=<PIN>` | Ejecuta la acción de un dispositivo |
| `/api/bridge/rule/<id>/run?token=<PIN>` | Ejecuta una regla |

`<PIN>` es el PIN o, mejor, el PIN de operador (`OPERATOR_PIN`), que no puede cambiar el show. Un token de acceso no sirve aquí. El id de un control está arriba en sus propiedades, en la página **Paneles**.

Para las teclas que se iluminan según el estado, Director también habla OSC con Companion: pon en `.env` `BRIDGE_OSC_PORT=<un puerto UDP libre>` y `BRIDGE_OSC_FEEDBACK=<dirección de Companion>:<su puerto de escucha OSC>`, y haz que Companion envíe el mensaje OSC `/subscribe` con la parte del estado que quiere como argumento, por ejemplo `obs.obs01`. El puerto OSC no pide PIN: úsalo solo en la red de control.

## MIDI

Una superficie de control es un dispositivo como cualquier otro: añádela en la página **Dispositivos** con el driver **MIDI controller**. Sus teclas y faders llegan como eventos para las reglas, y las reglas pueden iluminar sus teclas.

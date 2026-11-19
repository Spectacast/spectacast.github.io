# Dispositivos y drivers

<p class="lede">Todo lo que Director controla es un dispositivo: el OBS de una sala, su reunión, un receptor de teléfonos-micrófono, un receptor inalámbrico, un controlador MIDI. Un driver le dice a Director qué puede hacer un tipo de dispositivo y qué comunica.</p>

## Añadir un dispositivo

1. Abre la página **Dispositivos** y haz clic en **Añadir dispositivo**.
2. Elige el driver y escribe un nombre. El formulario muestra un campo por cada ajuste que necesita el driver, con su valor por defecto.
3. Guarda. La tarjeta se pone verde en cuanto el dispositivo responde. Haz clic en una tarjeta para ver su estado y su último error.

**editar** en una tarjeta cambia el nombre y los ajustes; Director vuelve a conectar al guardar. **Buscar en la red** y luego **buscar** muestra cada OBS y cada Spectacast Meet que responde en la red; **usar en el formulario** rellena el formulario con uno de ellos.

Las contraseñas no se guardan en el archivo del show. Ponlas en `C:\ProgramData\Spectacast\director\.env`, por ejemplo `OBS_PASSWORD=<contraseña>`, y después cierra la sesión y vuelve a iniciarla.

## Los drivers que trae Director

| Driver | Qué ve y qué hace Director |
|---|---|
| **OBS Studio** | Escenas, fuentes, audio, grabación y emisión de un OBS, por su servidor WebSocket |
| **NDI discovery** | Las fuentes NDI de la red, también a través de un NDI Discovery Server; sus imágenes en la página **Wall** |
| **Spectacast Meet** | Quién está en la reunión y en la sala de espera; admitir, silenciar y destacar; qué señal va a qué salida |
| **Spectacast Mic** | Los teléfonos conectados a un PC de sala como micrófonos e intercomunicación |
| **Translator** | Iniciar y detener una traducción, elegir los idiomas, leer lo que se oyó y lo que se dijo |
| **Sennheiser EW-DX receiver** | Silencio, ganancia, nivel, enlace de radio y batería de cada canal. Activa primero el acceso de terceros en el receptor |
| **MIDI controller** | Notas y controladores en ambos sentidos: faders y botones de una superficie de control |
| **Folder of files** | Los clips de una carpeta, local o compartida; un archivo copiado en ella aparece solo |
| **Recorder** | Graba la señal de la reunión de una sala en archivos de una hora |

Un dispositivo que no está en esta lista recibe un driver propio en la página **Drivers**, sin código: consulta [Tu propio driver](/es/ayuda/director-drivers/).

## Entradas desde fuera

Dos entradas permiten que otro sistema ponga algo en marcha en Director. Las dos están en la página **Dispositivos**, en **Entradas**.

- **webhook:** una llamada a `POST /api/hooks/<name>` lanza el evento `<name>`. El cuerpo JSON y los parámetros de la dirección llegan como campos del evento.
- **Entrada OSC:** fija un puerto, y cada mensaje OSC que llega a él se convierte en un evento con el nombre de su dirección: `/cue/go` pasa a ser `cue_go`.

Después, una regla reacciona al evento. Consulta [Reglas y scripts](/es/ayuda/director-rules/) y [API, webhooks y Stream Deck](/es/ayuda/director-api/).

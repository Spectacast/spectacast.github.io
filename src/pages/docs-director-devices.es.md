# Dispositivos y drivers

<p class="lede">Todo lo que Director controla es un dispositivo: el OBS de una sala, su reunión, un receptor de teléfonos-micrófono, un receptor inalámbrico, un controlador MIDI. Un driver le dice a Director qué puede hacer un tipo de dispositivo y qué comunica.</p>

## Añadir un dispositivo

1. Abre la página **Dispositivos** y ve al formulario **Añadir dispositivo**, debajo de las tarjetas.
2. Elige el driver y escribe un nombre. El formulario muestra un campo por cada ajuste que necesita el driver, con su valor por defecto.
3. Haz clic en **Añadir**. El punto de la tarjeta se pone verde en cuanto el dispositivo responde; la tarjeta muestra su estado y su último error.

**editar** en una tarjeta cambia el nombre y los ajustes; Director vuelve a conectar al guardar. **Buscar en la red** y luego **buscar** muestra cada OBS y cada Spectacast Meet que responde en la red; **usar en el formulario** rellena el formulario con uno de ellos.

La contraseña de OBS no se guarda en el archivo del show: ponla en `C:\ProgramData\Spectacast\director\.env` como `OBS_PASSWORD=<contraseña>`, y luego cierra la sesión y vuelve a entrar. La contraseña de un receptor Sennheiser o de un receptor de Mic se guarda en el archivo del show.

## Los drivers que trae Director

| Driver | Qué ve y qué hace Director |
|---|---|
| **OBS Studio** | Escenas, fuentes, audio, grabación y emisión de un OBS, por su servidor WebSocket |
| **NDI discovery** | Las fuentes NDI de la red, también a través de un NDI Discovery Server. Un control **Vista previa** muestra la imagen de cualquiera de ellas |
| **Spectacast Meet** | Quién está en la reunión y en la sala de espera; admitir, silenciar y destacar; qué señal va a qué salida |
| **Spectacast Mic** | Los teléfonos conectados a un PC de sala como micrófonos e intercomunicación |
| **Translator** | Iniciar y detener una traducción, elegir los idiomas, leer lo que se oyó y lo que se dijo |
| **Sennheiser EW-DX receiver** | Silencio, ganancia, nivel, enlace de radio y batería de cada canal. Activa primero 3rd Party Access en Sennheiser Control Cockpit (firmware 4.0.0 o posterior) |
| **MIDI controller** | Notas y controladores en ambos sentidos: faders y botones de una superficie de control |
| **Folder of files** | Los clips de una carpeta, local o compartida; un archivo copiado en ella aparece solo |
| **Recorder** | Graba la señal de la reunión de una sala en archivos de una hora |

Un dispositivo que no está en esta lista recibe un driver propio en la página **Drivers**, sin código: consulta [Tu propio driver](/es/ayuda/director-drivers/).

## Entradas desde fuera

Dos entradas permiten que otro sistema ponga algo en marcha en Director. Las dos están en la página **Dispositivos**, en **Entradas**.

- **Webhooks:** una llamada a `POST /api/hooks/<name>` lanza el evento `<name>`. El cuerpo JSON y los parámetros de la dirección llegan como campos del evento.
- **Entrada OSC:** fija un puerto, y cada mensaje OSC que llega a él se convierte en un evento con el nombre de su dirección: `/cue/go` pasa a ser `cue_go`.

Después, una regla reacciona al evento. Consulta [Reglas y scripts](/es/ayuda/director-rules/) y [API, webhooks y Stream Deck](/es/ayuda/director-api/).

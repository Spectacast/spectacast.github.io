# Guía de Meet

<p class="lede">Spectacast Meet se une a la reunión en línea desde el PC de sala y convierte a cada participante, la galería y cada pantalla compartida en una señal de vídeo para la sala.</p>

## Qué necesitas

- Un PC con Windows en la sala, en la misma red que la sala de control. También sirve un Mac, sin canales de interpretación.
- Una cuenta de Zoom que pueda organizar la reunión.
- OBS Studio en el mismo PC, o un mezclador que reciba NDI.

## Instalar e iniciar sesión

1. Ejecuta Spectacast Setup en el PC de sala y elige **Hall PC**. Setup instala lo que ejecuta el PC de sala, Meet incluido, y muestra un código para activar el PC como PC de sala en tu cuenta, en **Plan y PC**.
2. Inicia Meet. Su panel de control se abre en su propia ventana; el icono de la bandeja lo vuelve a mostrar.
3. Inicia sesión con Zoom y, en **Ajustes**, indica la reunión que organiza la sala: el número de reunión, el nombre que Meet muestra en la reunión, y el micrófono y los altavoces de la sala.

Meet se vuelve a iniciar solo tras un reinicio del PC, con los mismos ajustes y salidas.

## El panel de control

| Pestaña | Qué hace |
| --- | --- |
| Reunión | iniciar como anfitrión o unirse, salir o terminar, chat, silenciar a todos |
| Participantes | silenciar, vídeo, destacar, manos, roles, renombrar, sala de espera y salas para grupos, y un botón por salida para poner a alguien en ella |
| Salidas | cuántas señales y, para cada una, qué muestra, con qué resolución y con qué sonido |
| Ajustes | la reunión, el nombre, los dispositivos de audio, el inicio de sesión de Zoom y el registro |

## Las señales

Cada salida es una fuente NDI en la red. Para cada una, elige qué muestra:

- **Participante:** una persona, elegida por su nombre.
- **Orador activo:** quien habló por última vez.
- **Destacado:** la persona destacada, o una persona elegida cuando no hay nadie destacado.
- **Vista de Zoom:** la reunión dispuesta como en Zoom, sin nombres ni gráficos de Zoom: la pantalla compartida mientras alguien comparte, si no la galería o el orador.

Después elige la imagen (la cámara, o la pantalla compartida cuando la hay) y el sonido: el de esa persona, el de toda la reunión, o la reunión sin una persona, para un retorno que la sala ya oye. En OBS, añade la señal como fuente NDI.

## Desde la sala de control

En Director, Meet aparece en **Dispositivos** como cualquier otro dispositivo, y la tira de canal en **Paneles** muestra quién está en la reunión, quién habla y quién espera. Desde ahí el operador admite personas, silencia y pone a un orador en una salida, sin tocar el PC de sala.

## Canales de interpretación

Cuando la reunión tiene interpretación, Meet puede unirse como intérprete de un idioma y hablar con una voz de [Translator](/es/ayuda/translator/) o de una persona en la cabina. Los oyentes eligen el idioma en Zoom como siempre. Los canales de interpretación necesitan Meet en Windows.

{{shot:meet-interpreter-card|La tarjeta que Meet muestra en un canal de interpretación: el idioma e «Interpretación en vivo»}}

## Cuando algo no funciona

- **«Cannot connect to Zoom (no internet?)»:** Meet lo reintenta cada minuto; revisa el internet del PC de sala.
- **Una salida está en negro:** nadie corresponde a ella, por ejemplo porque la persona elegida se ha ido. Elige otra persona, o pon la salida en Orador activo.
- **Qué respondió Zoom:** el registro está al final de **Ajustes**.

# Spectacast Director

<p class="lede">La sala de control para eventos híbridos en directo. Un solo panel ve a la vez todos los PC de sala, la reunión en línea y los micrófonos, y las reglas se encargan de lo que, si no, alguien haría a mano muchas veces al día.</p>

{{cta}}

{{shot:director-channels|Spectacast Director con cuatro salas una al lado de otra: quién está en cada reunión, la sala de espera, Preview y Program}}

## Todas las salas en una pantalla

Cada sala tiene su propia franja: quién está en la reunión y quién habla, la sala de espera y el vestíbulo, Preview y Program, el rótulo y el streaming. Eliges a un ponente, lo pones en el aire con un toque, y la siguiente sala está justo al lado. Una sola persona puede seguir todo un congreso; en el congreso de 18 salas para el que se creó Director, así fue.

## Reglas para la rutina

Admitir al profesorado según llega, mantener la sala de espera como se configuró, devolver un clip a su sitio cuando un PC se reinicia, silenciar la sala mientras se reproduce un vídeo: las reglas reaccionan a lo que ocurre en la reunión, en OBS y en los micrófonos, y lo hacen siempre igual. Cada regla muestra cuándo se ejecutó por última vez y por qué.

{{shot:director-rules|Las reglas de Director: cada una con lo que la activa y su última ejecución}}

## Conectores, no una instalación fija

Director habla con cada herramienta mediante un conector, así que el vídeo, el audio y la plataforma de reuniones son una elección:

- **OBS Studio**: escenas, fuentes, salidas y audio en cada PC de sala
- **NDI**: vídeo y audio entre los PC, con un multiview de todas las salas
- **Spectacast Meet, Mic y Translator**: la reunión como señales separadas, teléfonos como micrófonos, traducción en directo
- **Sennheiser EW-DX**: los micrófonos inalámbricos de la sala, con nivel y batería
- **Dante, MIDI y carpetas**: audio en red, superficies de control, clips
- **Los tuyos**: cualquier equipo que hable HTTP, OSC o sockets

## Hecho para la sala

Director funciona en un PC de la sala de control y los PC de sala en la red del propio recinto, así que el evento sigue aunque falle internet. La página de la flota muestra de un vistazo el PC, la reunión y la salida de cada sala; los paneles se montan con bloques, de modo que una sala nueva es una copia más, no un diseño nuevo. El panel habla español, inglés, alemán e italiano.

{{shot:director-fleet|La flota en Director: la reunión, las personas, la sala de espera y la salida de cada sala}}

{{plans:Director,Show,Complete}}

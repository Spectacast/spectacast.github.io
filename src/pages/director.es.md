# Spectacast Director

<p class="lede">La sala de control para eventos híbridos en directo. Un solo panel ve a la vez todos los PC de sala, la reunión en línea y los micrófonos, y las reglas se encargan de lo que, si no, alguien haría a mano muchas veces al día.</p>

{{cta}}

{{loop:director-speaker|Elige a una ponente, abre su micrófono y ponla en primer plano. Tres toques.|Grabación de pantalla de Director: el operador elige a la Dra. Elena Ortega en la Sala A, abre su micrófono y la pone en primer plano}}

## Todas las salas en una pantalla

Cada sala tiene su propia franja: quién está en la reunión y quién habla, la sala de espera y el vestíbulo, Preview y Program, el rótulo y el streaming. Eliges a un ponente, lo pones al aire con un toque, y la siguiente sala está justo al lado. Una sola persona puede seguir todo un congreso; en el congreso de 18 salas para el que se creó Director, así fue.

{{closeup:director-hall|Primer plano de la Sala A y la Sala B en Director: las dos al aire, cuatro personas en cada reunión con su nivel de micrófono, y la sala de espera|**Rojo significa al aire**, con la reunión y los micrófonos.|**Quién está en la reunión**, cada uno con su nivel de micrófono en vivo.|**La sala de espera**: un toque deja entrar a un ponente.}}

## Reglas para la rutina

Admitir al profesorado según llega, mantener la sala de espera como se configuró, devolver un clip a su sitio cuando un PC se reinicia, silenciar la sala mientras se reproduce un vídeo: las reglas reaccionan a lo que ocurre en la reunión, en OBS y en los micrófonos, y lo hacen siempre igual. Cada regla muestra cuándo se ejecutó por última vez y por qué.

{{story:rule|Animación: la Dra. Elena Ortega entra en la sala de espera de la Sala A, la regla «Admitir automáticamente» se ilumina y ella aparece en la reunión}}

{{loop:director-clip|Pon un clip al aire: el micrófono de la sala se silencia solo.|Grabación de pantalla de Director: el operador pone el clip en Program en la Sala A, la sala pasa a VOD y su micrófono se silencia; al volver a la reunión, se abre de nuevo}}

## Conectores, no una instalación fija

Director habla con cada herramienta mediante un conector, así que el vídeo, el audio y la plataforma de reuniones son una elección:

- **OBS Studio**: escenas, fuentes, salidas y audio en cada PC de sala
- **NDI**: vídeo y audio entre los PC, con un multiview de todas las salas
- **Spectacast Meet, Mic y Translator**: la reunión como señales separadas, teléfonos como micrófonos, traducción en directo
- **Sennheiser EW-DX**: los micrófonos inalámbricos de la sala, con nivel y batería
- **MIDI y carpetas**: superficies de control y los clips que aparecen durante el evento
- **Dante**: el audio en red de la sala, mediante Dante Virtual Soundcard en un PC
- **Los tuyos**: cualquier equipo que hable HTTP, OSC o sockets

Cómo conectar un equipo tuyo, programar las reglas y usar la API: [Hecho para ampliarse](/es/desarrolladores/).

## Hecho para la sala

Director funciona en un PC de la sala de control y habla con los PC de sala por la red del propio recinto, así que el evento sigue aunque falle internet. La página de la flota muestra de un vistazo el PC, la reunión y la salida de cada sala; los paneles se montan con bloques, de modo que una sala nueva es una copia más, no un diseño nuevo. El panel habla español, inglés, alemán e italiano.

{{closeup:director-fleet|Primer plano de la página de la flota de Director: cuatro salas, cada una en línea y en su reunión, con niveles de micrófono y sala de espera|**El PC de cada sala**: en línea y en su reunión.|**Quién habla**: una barra por micrófono, en vivo.|**La sala de espera**: admite a todos, o actívala y desactívala, desde aquí.}}

{{plans:Director,Show,Complete}}

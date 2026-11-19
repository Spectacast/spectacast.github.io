# Hecho para ampliarse

<p class="lede">En todo recinto hay un equipo con el que nadie contaba. Spectacast Director está hecho para que lo conectes tú: describe su protocolo en un formulario, resuelve con un script lo que los formularios no saben decir y maneja todo desde tus propios sistemas con su API.</p>

{{cta}}

## Conecta un equipo sin código

En la página Drivers describes el protocolo de un dispositivo: los comandos que acepta y los mensajes que devuelve. Director habla OSC, UDP, TCP, HTTP y WebSocket, lo que cubre la mayoría de mesas de luces, mezcladores de audio, mezcladores de vídeo y matrices. Una vez descrito, el dispositivo tiene botones, estado en vivo y reglas como los incluidos.

Lo pruebas con el dispositivo real, viendo en directo cada mensaje que entra y que sale, y compartes un driver terminado como un solo archivo.

[Cómo describir un driver →](/es/ayuda/director-drivers/)

## Reglas, y scripts cuando las reglas no bastan

Las reglas reaccionan a lo que pasa en las salas: alguien entra en la sala de espera, un ponente toma la palabra, una fuente se cae. La mayoría se construye con formularios. Donde la lógica es la tuya, un paso puede ser unas pocas líneas de JavaScript con todo el estado a mano.

{{shot:director-rules|Las reglas de Director: cada una con lo que la activa y su última ejecución}}

[Reglas y scripts →](/es/ayuda/director-rules/)

## Una API para tus propios sistemas

Todo lo que hace el dashboard pasa por una API HTTP en el PC de control, y un WebSocket envía cada cambio en cuanto ocurre. Un sistema de inscripciones, un controlador de show o un script puede leer el estado de cada sala, pulsar un botón, fijar una variable o ejecutar una regla, cada uno con un token que limita lo que puede hacer.

[La API →](/es/ayuda/director-api/)

## Webhooks y entrada OSC

Otro sistema pone algo en marcha en Director con una sola llamada: un webhook por HTTP o un mensaje OSC. El programa del congreso puede anunciar una sesión, y una regla pone el título correcto en la sala correcta.

## Stream Deck y MIDI

Una tecla de Stream Deck pulsa cualquier control del dashboard a través de Bitfocus Companion, sin instalar nada más. Una superficie de control MIDI da al operador faders y teclas de verdad, y las reglas pueden iluminarlos.

## Tus propios paneles

Los paneles del dashboard los organizas tú: botones, selecciones, campos de texto, medidores de nivel e imágenes en directo, construidos una vez como bloque y colocados una vez por sala.

{{shot:director-panels|Un panel de Director con cuatro salas: un bloque por sala, con su reunión, su sala de espera, Preview y Program}}

[Paneles →](/es/ayuda/director-panels/)

## ¿Tu equipo no se puede conectar así?

Algunos equipos necesitan la biblioteca de su fabricante. Esos drivers están integrados en Director, como los de OBS Studio, NDI y Sennheiser EW-DX.

[Dinos qué quieres controlar →](/es/contacto/)

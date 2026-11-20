# Paneles

<p class="lede">Un panel es una página de controles que colocas tú: botones, interruptores, selecciones, campos de texto y los recuadros de cada sala. Los paneles del show de ejemplo son un punto de partida, y todos se pueden cambiar.</p>

{{shot:director-panels|Un panel de Director con cuatro salas: un bloque por sala, con su reunión, su sala de espera, Preview y Program}}

## Editar un panel

En la página **Paneles** haz clic en **Editar**. Ahora un clic en una celda vacía añade un control, y un clic en un control abre sus propiedades.

- Selecciona varios controles con Mayús-clic o arrastrando un rectángulo, y muévelos, cópialos o bórralos juntos.
- **Deshacer** y **Rehacer** retroceden y avanzan hasta cien pasos.
- **Guardar** conserva los cambios para todos los dashboards; **Descartar** los desecha.

**+ panel** añade una página. Quien inicia sesión con el PIN de operador ve los paneles y nada más.

{{closeup:director-build-panel|Primer plano del editor de paneles de Director: la fila de bloques ya hechos, la cuadrícula del panel con celdas vacías y el botón Guardar|**Bloques**: una sala entera, una reunión o un monitor, hechos una vez y colocados donde hagan falta.|**Haz clic en una celda vacía** para añadir un control o colocar un bloque, o en un control para cambiarlo.|**Guarda**, y el panel está listo para usar.}}

## Controles

| Control | Qué hace |
|---|---|
| **Botón** | Ejecuta sus pasos al pulsarlo |
| **Interruptor** | Una lista de pasos para encender y otra para apagar |
| **Selección (opciones)** | Una fila de opciones: una lista fija o una en vivo, como las escenas de un OBS o las personas de una reunión |
| **Entrada de texto** | Un campo con un botón para aplicar, para un rótulo o un nombre |
| **Etiqueta** | Muestra un texto o un valor |
| **Estado del dispositivo** | Muestra si un dispositivo está conectado |
| **Vista previa (imagen de un dispositivo)** | La imagen en directo de un OBS o de una fuente NDI |
| **Mezclador (entradas de audio de un dispositivo)** | Faders y silencio para las entradas de audio de un dispositivo |
| **Marco (grupo)** | Un borde con título alrededor de los controles que van juntos |
| **Bloque** | Un conjunto de controles que se construye una vez y se coloca muchas veces |

## Qué hace una pulsación

Una pulsación ejecuta una lista de pasos, de arriba abajo:

- una **acción** sobre un dispositivo, como «cambiar la escena de programa»;
- una **espera**;
- **fijar una variable**;
- un **si** con una lista para el sí y otra para el no;
- pasos que se ejecutan **en paralelo**, o una vez **por cada** elemento de una lista.

**Preguntar antes** hace que el dashboard pregunte antes de ejecutar los pasos: para los botones que nadie debe pulsar por error.

## Respuesta visual: el aspecto de un control

Las entradas de **Respuesta visual** cambian el color y el texto de un control según el estado en vivo: rojo mientras una sala está al aire, un nombre cuando hay alguien en la sala de espera. Las entradas se comprueban desde arriba, y gana la primera que se cumple.

## Bloques: una tira para cada sala

Construye una vez los controles de una sala, selecciónalos y haz clic en **Crear bloque**. Los dispositivos que nombran pasan a ser los **Valores** del bloque. Coloca el bloque una vez por sala y da a cada copia sus propios dispositivos. Un cambio en el bloque llega a todas las salas a la vez.

## Variables

La página **Variables** guarda valores que comparten los paneles y las reglas: el clip elegido, el ponente que tiene la palabra. **Añadir variable** crea una, con su tipo y su valor inicial.

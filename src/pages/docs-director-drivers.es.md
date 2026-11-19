# Tu propio driver

<p class="lede">La página Drivers describe el protocolo de un dispositivo sin código. Una vez descrito, el dispositivo tiene acciones, eventos y estado como uno de los incluidos, y los paneles y las reglas lo usan igual.</p>

Un driver definido por ti habla uno de cinco transportes: **OSC**, **UDP**, **TCP**, **HTTP** o **WebSocket**. Con eso se cubre la mayoría de mesas de luces, mezcladores de audio, mezcladores de vídeo, matrices y sistemas de control de edificios.

## 1. Crear el driver

En la página **Drivers** haz clic en **+ driver por…** y elige el transporte. Ponle un nombre al driver y enumera los ajustes que pide cada dispositivo suyo: un host, un puerto, una clave de API. Un ajuste tiene un valor por defecto o está marcado con **oblig.** (obligatorio), y las plantillas de abajo lo leen como `config.<id>`.

## 2. Comandos

Haz clic en **+ comando** por cada cosa que se le puede ordenar al dispositivo. Un comando se convierte en una acción que los botones y las reglas pueden ejecutar.

- Sus **parámetros** son campos con tipo, que el mensaje lee como `params.<id>`.
- Su **mensaje** es una plantilla. En OSC es una dirección con argumentos con tipo, como `/cue/{{params.cue}}/go`. En HTTP es un método, una ruta, cabeceras y un cuerpo. En UDP, TCP y WebSocket es una línea de texto, o bytes escritos en hexadecimal para un protocolo binario.

## 3. Retorno

Haz clic en **+ entrada de retorno** por cada mensaje que el dispositivo devuelve. Una entrada reconoce un mensaje y dice qué hacer con él.

- **Reconocer** por un patrón de dirección OSC (`/cue/{n}/active`, donde `{n}` captura una parte de la dirección), por una expresión regular sobre texto o por una expresión sobre un mensaje JSON.
- **Fijar estado:** escribir valores del mensaje en el estado del dispositivo, donde los paneles los muestran y las reglas los leen.
- **Lanzar un evento** al que una regla puede reaccionar.

Un driver HTTP también puede **sondear**: consulta una dirección cada pocos segundos y pasa la respuesta por las mismas entradas.

## 4. En línea o fuera de línea

Los dispositivos TCP y WebSocket están en línea mientras la conexión está abierta, y Director vuelve a conectar por sí solo. Los dispositivos UDP, OSC y HTTP necesitan un **latido**: un comando enviado a intervalos cuya respuesta demuestra que el dispositivo está ahí. Sin él cuentan como en línea.

## 5. Probarlo con el dispositivo real

Haz clic en **Crear driver** y añade después un dispositivo con tu driver en la página **Dispositivos**. De vuelta en la página **Drivers**, haz clic en **probar** en la tarjeta del driver, elige el dispositivo y haz clic en **registrar mensajes**. Cada mensaje que entra y que sale aparece en directo, y cada uno de los que entran muestra qué entradas de retorno coinciden con él y qué fijarían. **Enviar prueba** ejecuta un comando con los parámetros que escribas.

## 6. Compartirlo

**exportar** descarga la definición como un archivo JSON; **importar JSON** añade una a otro show. Las definiciones se guardan dentro del archivo del show, así que un show lleva consigo sus drivers.

Dos ejemplos para importar y adaptar: [un dispositivo OSC genérico](/examples/drivers/generic-osc.json) y [un dispositivo HTTP cuyo estado se consulta a intervalos](/examples/drivers/http-example.json).

## Cuando esto no basta

Un dispositivo que necesita la biblioteca de su fabricante, o un protocolo que estos cinco transportes no pueden llevar, necesita un driver integrado en Director. [Dinos](/es/contacto/) qué dispositivo quieres controlar.

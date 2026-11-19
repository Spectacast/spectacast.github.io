# Guía de Translator

<p class="lede">Translator escucha a quien habla y dice lo que dice en otro idioma, en directo, por cualquier salida de audio. Un Translator, llamado canal, por idioma.</p>

## Qué necesitas

- Un PC con Windows en la sala o en la sala de control, instalado con Spectacast Setup y activado en tu cuenta.
- Un plan con Translator: sus minutos llegan con la licencia del PC, sin configurar nada. O tu propia clave de Google Gemini o de OpenAI.
- Una entrada con la voz de quien habla: un micrófono, el mezclador, un teléfono a través de [Mic](/es/ayuda/mic/) o una señal por NDI.

## La página de control

Cada canal tiene su propia página de control, en **http://127.0.0.1:4720** para el primer canal de ese PC. Elige:

1. la **entrada**: una tarjeta de sonido, o una fuente NDI como un participante de [Meet](/es/ayuda/meet/);
2. la **salida**: una tarjeta de sonido, un cable virtual hacia OBS o el mezclador, o el canal de interpretación de Meet;
3. el **idioma** en que hablar;

y pulsa **Iniciar**. La página muestra cada frase dos veces, tal como se oyó y tal como se dijo, mientras se habla.

{{shot:translator|La página de control de Translator: lo que se oyó en italiano y lo que se dijo en inglés, línea a línea}}

## Motores

El motor decide cómo suena Translator y lo rápido que responde. Google Gemini es el predeterminado; OpenAI es el otro. Los motores de **intérprete** actúan como una intérprete de congreso: dales el **Tema** de la sesión y un glosario de nombres y términos técnicos, uno por línea, y los usan.

## Sentido invertido

Mientras un canal funciona, un segundo modelo lee lo que se oyó junto a lo que se dijo y marca en rojo los puntos donde la traducción dice algo distinto: un «no» perdido, un número, izquierda por derecha, un nombre. No cambia nada de lo que dice el canal; es para quien lo vigila. La casilla **Avisar cuando el sentido se invierte** lo desactiva.

## En la reunión

Para dar un idioma a quienes escuchan en la reunión en línea, pon la salida del canal en el canal de interpretación de Meet. Meet se une como intérprete de ese idioma, y quienes escuchan eligen el idioma en Zoom. Consulta [Meet](/es/ayuda/meet/).

## Tras un reinicio

Un canal recuerda lo que estaba haciendo. Tras un reinicio del PC vuelve con la misma entrada, salida e idioma, y arranca de nuevo si estaba en marcha; lo reintenta durante diez minutos mientras falte una tarjeta de sonido o la red.

## Minutos

Cada minuto que habla un canal cuenta, por idioma. Los planes con Translator incluyen {{INCLUDED_MINUTES}} minutos por sala; tu cuenta muestra cuántos has usado. Consulta [Cuenta y facturación](/es/ayuda/cuenta-y-facturacion/).

# Seguridad y datos

<p class="lede">La mayor parte de Spectacast funciona en tus propios ordenadores, en la sala. Esta página explica con palabras sencillas qué se queda allí, qué sale a internet y quién lo trata. El texto vinculante es la <a href="{{PRIVACY_URL}}">Política de privacidad</a>.</p>

## Qué se queda en la sala

Director, Meet y el receptor de Mic son programas instalados en tus PC de sala. El vídeo, el audio y las señales de la reunión viajan entre esos PC por la red del propio recinto, y las grabaciones son archivos en tus propios discos. Nosotros no recibimos nada de eso.

Los teléfonos que hacen de micrófono se emparejan con el PC con el que hablan, y su audio viaja cifrado de extremo a extremo.

La reunión en línea es una reunión de Zoom corriente, en tu propia cuenta de Zoom y con las condiciones de Zoom.

## Qué sale a internet

| Qué | Adónde va | Para qué |
|---|---|---|
| **Comprobación de la licencia:** la clave de licencia, un identificador aleatorio del PC, el programa y su versión, la sala y si está en el aire | Nuestro servidor de licencias en la Unión Europea | Para comprobar que tu plan está activo y cuántas salas se usan |
| **Tu cuenta:** nombre, correo electrónico, organización, país, plan | Nuestro servidor de cuentas en la Unión Europea | Para gestionar tu cuenta y tus licencias |
| **Spectacast Pass:** asistentes, acreditaciones, lecturas en las puertas, asistencia | Nuestro servidor de Pass en la Unión Europea | Alojamos Pass para el organizador del evento |
| **Spectacast Translator:** la voz que hay que traducir | Google u OpenAI, según el motor que elijas para cada idioma | El motor devuelve la traducción en directo |
| **Un informe**, cuando pulsas «Enviar informe»: los registros y las versiones del programa | Nuestro servidor en la Unión Europea | Para encontrar un fallo; se borra en un plazo de 90 días |
| **Pagos** | Paddle, que vende Spectacast como Merchant of Record | Paddle cobra el pago; nunca vemos el número de tu tarjeta |

El contenido de tu evento nunca forma parte de la comprobación de la licencia. El sitio web no usa cookies, analítica ni publicidad.

## Cuando se cae internet

Una sala que pierde la conexión sigue funcionando: una licencia de pago funciona 14 días sin internet. Los teléfonos de las puertas de Pass siguen decidiendo por su cuenta y envían sus lecturas cuando vuelve la red.

## Cómo se protegen los datos

- Todas las conexiones con nuestros servidores van cifradas (HTTPS).
- Las contraseñas se guardan solo como hashes con sal, nunca como texto.
- Los servidores están en la Unión Europea, y solo acceden las personas que mantienen el servicio.
- Las bases de datos de Pass y de las cuentas se copian cada noche.
- La voz que se envía a los motores de Translator viaja por una conexión cifrada, y según sus condiciones de API ni Google ni OpenAI la usan para entrenar sus modelos generales.

## Quién trata datos por nosotros

| Proveedor | Para qué | Dónde |
|---|---|---|
| **Hetzner Online GmbH** | Alojamiento de Pass, del servidor de cuentas y de licencias y de este sitio web | Unión Europea |
| **Google (Gemini API) y OpenAI (Realtime API)** | Traducción de voz, cuando usas los minutos incluidos en tu plan | Puede ser fuera de la Unión Europea, incluidos los Estados Unidos |
| **Brevo (Sendinblue SAS)** | Envío de los correos de tu cuenta y de las acreditaciones que Pass envía por correo a los asistentes | Francia |
| **Porkbun, LLC** | Reenvío del correo enviado a nuestras direcciones de spectacast.com | Estados Unidos |

Paddle no está en esta lista porque trata tus datos de pago como responsable por cuenta propia. Cuando usas Translator con tu propia clave de Google o de OpenAI, contratas directamente con el motor y nosotros no recibimos nada.

## Los datos de tus asistentes

Para las personas de tu evento, tú eres el responsable del tratamiento y nosotros tu encargado (art. 28 RGPD). Tratamos sus datos solo siguiendo tus instrucciones, y tú decides cuánto tiempo los conserva Pass. Enviamos el contrato de encargo del tratamiento a quien lo pida: escribe a [privacy@spectacast.com](mailto:privacy@spectacast.com).

Cuánto tiempo se conserva cada tipo de dato figura en la [Política de privacidad]({{PRIVACY_URL}}).

## Avisar de un problema de seguridad

Si encuentras una vulnerabilidad en Spectacast, escribe a [support@spectacast.com](mailto:support@spectacast.com) antes de hacerla pública, para que podamos corregirla primero.

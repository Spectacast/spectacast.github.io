# Política de privacidad

Última actualización: {{date}}

Esta política explica qué datos personales trata Spectacast, por qué y qué derechos tienes. Abarca el sitio web spectacast.com, la cuenta de cliente de Spectacast, Spectacast Pass, Spectacast Translator y la comprobación de la licencia en Spectacast Director, Meet y Mic. La aplicación para teléfono Spectacast Mic tiene su propia política breve, enlazada al final.

## Quiénes somos

**Spectacast** es el responsable del tratamiento de los datos descritos aquí, salvo que una sección indique otra cosa. Contacto de privacidad: {{PRIVACY_EMAIL}}.

## En resumen

- La mayor parte de Spectacast funciona en los ordenadores de nuestros clientes. El vídeo, el audio y las reuniones de un evento se quedan allí y no los recibimos.
- Tres partes envían datos a internet: **Spectacast Pass**, que alojamos nosotros, **Spectacast Translator**, que envía voz a un motor de IA externo, y **Spectacast Meet**, que inicia sesión en tu cuenta de Zoom a través de nuestro servidor.
- Para los datos de las personas de un evento (asistentes, ponentes), **el organizador del evento es el responsable del tratamiento y nosotros actuamos como su encargado** (art. 28 RGPD).
- No vendemos datos personales, no mostramos publicidad ni usamos cookies de seguimiento.

## 1. Nuestros clientes: cuenta, facturación y soporte

| Datos | Finalidad | Base jurídica | Conservación |
|---|---|---|---|
| Nombre, correo electrónico, organización (si la tienes), país, tu plan | Gestionar tu cuenta y tu licencia | Contrato (art. 6.1.b) | Mientras seas cliente y 12 meses más |
| Registros de pedidos y pagos | Contabilidad e impuestos | Obligación legal (art. 6.1.c) | 10 años (Código de Comercio y Código Tributario alemanes) |
| Correos electrónicos y solicitudes de soporte | Responderte | Contrato, interés legítimo (art. 6.1.f) | 24 meses desde el último mensaje |

**Paddle.com** vende Spectacast como nuestro revendedor y Merchant of Record. Paddle recoge directamente tus datos de pago, tu dirección de facturación y tu número de identificación fiscal, y es responsable de ellos según su propio [aviso de privacidad](https://www.paddle.com/legal/privacy). De Paddle recibimos tu nombre, tu correo electrónico, tu país, lo que compraste y el estado del pago, nunca el número de tu tarjeta.

## 2. La comprobación de la licencia (Director, Meet, receptor de Mic, Translator)

Los programas instalados contactan con nuestro servidor de licencias al arrancar y periódicamente. Envían la clave del ordenador, el identificador que Windows da al ordenador (solo guardamos su hash), el nombre del ordenador y la versión del programa. Nuestro servidor ve la dirección IP del ordenador. Usamos estos datos para comprobar que el plan está activo y cuántas salas están en uso (contrato, art. 6.1.b) y conservamos el registro durante 12 meses. Una vez al día envían también los totales de uso, sin ningún contenido del evento: minutos en emisión, minutos de Translator por idioma y acreditaciones leídas. Cuando se abre un reembolso o una disputa de pago sobre tu pedido, podemos entregar a Paddle un resumen de este registro, como los ordenadores activados y las horas de uso, para mostrar si el plan se usó (interés legítimo, art. 6.1.f).

Cuando inicias sesión en Zoom desde Spectacast Meet, el inicio de sesión pasa por nuestro servidor. Este guarda tu nombre y tu correo electrónico de Zoom, tus números de usuario y de cuenta de Zoom y la autorización que Zoom da a Meet para organizar tus reuniones, para que el ordenador de la sala pueda organizar la reunión en tu cuenta (contrato, art. 6.1.b). Los eliminamos cuando desconectas Meet de Zoom.

## 3. Spectacast Pass: datos de asistentes

Alojamos Pass para el organizador del evento. **El organizador es el responsable del tratamiento** de los datos de los asistentes y decide qué se recoge y por qué; **nosotros los tratamos por cuenta del organizador**, siguiendo solo sus instrucciones, conforme a un contrato de encargo del tratamiento, que enviamos a petición ({{PRIVACY_EMAIL}}).

Datos que un organizador suele guardar en Pass:

- nombre, correo electrónico, organización, categoría (por ejemplo ponente, congresista, personal) y código de acreditación del asistente;
- las horas en que se leyó cada acreditación en cada puerta, y las sesiones y el tiempo en cada sala calculados a partir de ellas;
- los certificados de asistencia elaborados con esos registros;
- los nombres del personal del organizador que usa las páginas de administración y los lectores de las puertas.

Dónde se guardan: en servidores de **Hetzner Online GmbH** en la Unión Europea. Los teléfonos de las puertas conservan las lecturas sin conexión hasta que pueden enviarlas, y después solo lo que necesita la pantalla del lector.

Cuánto tiempo: lo decide el organizador. Por defecto, los datos de un evento se conservan 24 meses después del evento, lo que cubre los informes de formación médica continuada (FMC), y se eliminan cuando el organizador elimina el evento o 30 días después de que termine su plan.

Los asistentes que quieran ver, corregir o eliminar sus datos deben pedirlo al organizador del evento. Si nos escriben a nosotros, trasladamos la solicitud al organizador.

## 4. Spectacast Translator: voz enviada a motores de IA

Translator escucha un micrófono, una señal de sala o una reunión y devuelve una traducción en directo. Para ello, **la voz se envía en directo, por una conexión cifrada, al motor de IA elegido para ese idioma**:

- **Google** (Gemini API), Google Ireland Limited / Google LLC, o
- **OpenAI** (Realtime API), OpenAI Ireland Ltd / OpenAI, L.L.C.

El motor devuelve audio traducido y una transcripción escrita. Translator muestra la transcripción en la pantalla del operador y la guarda en el registro del programa en el ordenador de la sala; no nos envía audio ni transcripciones.

Mientras la comprobación de sentido invertido está activada, Translator envía además la transcripción escrita del último minuto a un modelo de texto, que marca los puntos donde la traducción dice algo distinto de lo que dijo el ponente: un modelo de Google o, si el cliente ha puesto una clave de Anthropic en el ordenador, de Anthropic (Anthropic, PBC). La comprobación se puede desactivar en cada pista.

Cuando el plan incluye minutos de traducción, el programa usa **nuestra** cuenta del motor: el motor trata la voz como nuestro subencargado, y **nosotros actuamos como encargado del organizador del evento**, que es el responsable de las voces de los ponentes. Cuando el cliente usa **sus propias** claves del motor, contrata directamente con el motor y nosotros no recibimos nada.

Qué hacen los motores con ella: según sus condiciones de API publicadas a 17 de noviembre de 2026, ni Google ni OpenAI usan estos datos de API para entrenar sus modelos generales. Ambos los conservan durante un tiempo limitado para detectar abusos y luego los eliminan: OpenAI hasta 30 días, Google hasta 55 días. Mantenemos desactivado el registro opcional de solicitudes en nuestro proyecto de Google. Sus servidores pueden estar fuera de la UE (incluidos los Estados Unidos); las transferencias se basan en el Marco de Privacidad de Datos UE-EE. UU. y en las Cláusulas Contractuales Tipo de la Comisión Europea.

La voz puede contener datos personales, incluidos datos de salud en charlas médicas (art. 9 RGPD). El organizador debe informar a los ponentes de que su voz es traducida por un motor de IA externo y no debe traducir voz que no tenga derecho a tratar. El organizador puede desactivar Translator para cualquier ponente.

## 5. El sitio web spectacast.com

Nuestro servidor registra la dirección IP, la página, la fecha y el navegador de cada visita en su registro de accesos, para mantener el sitio seguro y en funcionamiento (interés legítimo, art. 6.1.f), y elimina el registro a los 14 días. El sitio no instala cookies ni usa analítica o publicidad. Tu cuenta y las páginas de administración de Pass guardan en tu navegador una cookie de inicio de sesión, necesaria para que funcionen.

## 6. Quién más recibe datos

- **Paddle.com** (Merchant of Record): pedidos, pagos, facturas, impuestos.
- **Hetzner Online GmbH**, Alemania: alojamiento de Pass, del servidor de licencias y de este sitio web.
- **Google** y **OpenAI**: voz para traducir, como se describe arriba.
- **Brevo** (Sendinblue SAS), Francia: envía los correos de tu cuenta y las acreditaciones que Pass envía por correo electrónico a los asistentes.
- **Porkbun, LLC**, Estados Unidos: reenvía a nuestro buzón el correo enviado a nuestras direcciones de spectacast.com.
- Nuestro asesor contable y nuestros abogados, y las autoridades públicas cuando la ley lo exija.

Cada proveedor trabaja con un contrato que protege los datos. La lista actual de subencargados está disponible a petición.

## 7. Seguridad

Los datos viajan cifrados (HTTPS). Los datos de Pass están en servidores en la UE, con acceso limitado a las personas que gestionan el servicio, protegidos por claves y con copia de seguridad cada noche. Los micrófonos de teléfono están emparejados y cifrados de extremo a extremo con el ordenador con el que hablan.

## 8. Tus derechos

Según el RGPD puedes pedirnos acceder a tus datos, rectificarlos o suprimirlos, limitar su uso u oponerte a él, y recibirlos en un formato portable. Cuando nos basamos en el consentimiento, puedes retirarlo en cualquier momento. Escribe a {{PRIVACY_EMAIL}}: respondemos en el plazo de un mes. También puedes presentar una reclamación ante una autoridad de protección de datos, en particular la del lugar donde vives o trabajas.

Para los datos de Pass o de una sesión traducida, el responsable es el organizador del evento: escríbele primero a él.

## 9. Menores

Spectacast es una herramienta para organizar eventos. No está dirigida a menores, y solo una persona mayor de edad puede comprar un plan.

## 10. Cambios

Si esta política cambia, publicamos aquí la nueva versión con una nueva fecha y avisamos a los clientes por correo electrónico cuando el cambio es importante.

La política de privacidad de la aplicación para teléfono Spectacast Mic: {{MIC_PRIVACY_URL}}.

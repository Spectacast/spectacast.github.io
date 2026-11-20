# Guía de Pass

<p class="lede">Configura un evento en Pass, convierte teléfonos en lectores para las puertas y obtén la asistencia después. Pass funciona en el navegador, en spectacast.com/pass.</p>

## 1. El evento

Inicia sesión en [spectacast.com/pass](/pass/) con tu cuenta de Spectacast y crea un **Nuevo evento**. Después, en **Configuración**:

- **Zonas:** las salas donde se cuenta la presencia.
- **Accesos:** uno por entrada, cada uno en una zona.
- **Sesiones:** el programa. Marca con **Cuenta** las sesiones que cuentan para la asistencia.
- **Categorías:** los tipos de asistentes, como ponentes, congresistas o personal.

La lista de arriba dice qué falta todavía.

## 2. Asistentes y credenciales

En **Asistentes**:

- **+ Persona o importar** añade a alguien a mano, por ejemplo quien se inscribe en el mostrador, o lee un CSV, o un Excel guardado como CSV, con encabezados como First name, Last name, Email, Category e ID (también sirven los italianos). Las demás columnas se guardan como campos que las reglas y los mensajes pueden usar. Importar otra vez actualiza a las mismas personas.
- Las **Fuentes** traen la lista de una web de inscripción por sí solas, y las **Claves para otros sistemas** permiten que una web envíe sus inscripciones. Pide al proveedor de tu web de inscripción, o a nosotros, que las conecte.

Cada asistente recibe una credencial con un código QR. **Imprimir todas las credenciales** las imprime, sobre tu propio fondo si subes uno, o **Credenciales por correo** envía a cada persona la suya.

## 3. Las puertas

En cada puerta usa un teléfono o una tableta, o un lector de teclado conectado a un portátil.

1. En **Configuración**, **Accesos**, pulsa **Configurar un teléfono** para esa puerta.
2. Apunta la cámara del teléfono al código QR de la pantalla y abre el enlace. La app de la puerta se abre en ese acceso, sin escribir nada.
3. Añádela a la pantalla de inicio, para que se abra como una app.

La puerta responde a cada credencial al instante, a pantalla completa en verde, ámbar o rojo, con un sonido y el nombre de la persona. Si se cae la red, la puerta sigue decidiendo por sí misma y envía sus lecturas cuando vuelve la red.

{{closeup:pass-answers|Las tres respuestas de la app de puerta, cada una en un teléfono: verde para una entrada con el nombre de la persona, ámbar cuando se lee una credencial que ya está dentro, con un botón para continuar, y rojo para una credencial que no se encuentra|**Verde**: adelante, con un saludo por su nombre.|**Ámbar**: mira primero. Esta credencial ya está dentro, y la puerta espera un toque.|**Rojo**: no válida, con lo que hay que hacer.}}

Un **lector de teclado** funciona en la misma página de la puerta: configúralo para que envíe Enter tras cada código. Un lector en modo de almacenamiento, en una puerta sin pantalla, se vuelca después en **Subir lecturas**.

## 4. Reglas

Lo que dice una puerta lo deciden las **Reglas**, probadas de arriba abajo; la primera que encaja decide. Un evento nuevo empieza con reglas sensatas: ignorar una lectura doble, rechazar credenciales desconocidas o canceladas, avisar cuando alguien ya está dentro, rechazar una sala llena, dar la bienvenida a los demás. Añade las tuyas, por ejemplo una sala solo para una categoría, y prueba cualquier credencial con **Probar una lectura** antes de abrir las puertas.

## 5. Durante el evento

**En directo** muestra cuántas personas hay en cada sala, las últimas lecturas, los teléfonos de las puertas y si están conectados. Lo que una puerta decidió sin conexión de forma distinta al servidor aparece en **Por revisar**.

## 6. Después

Los **Informes** dan, por persona, los minutos y el porcentaje en cada sesión, listos para Excel. En **Certificados**, indica qué necesita una persona para un certificado de asistencia; quien lo cumple descarga el suyo.

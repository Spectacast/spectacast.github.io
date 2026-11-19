# Guía de Director

<p class="lede">De un PC de control nuevo a tu primera sala al aire en una media hora.</p>

Necesitas un PC con Windows 10 u 11 para la sala de control y, para cada sala, un PC con Windows con OBS Studio y Spectacast Meet. Todos los PC deben estar en la misma red.

## 1. Instalar en el PC de control

1. Descarga Spectacast Setup desde [Descargas](/es/descargas/) y descomprímelo.
2. Haz doble clic en **Setup.cmd**. Windows pide permisos de administrador.
3. Elige **1, Control room**.
4. Setup instala Director, abre sus puertos en el cortafuegos y lo inicia. Luego muestra un código como `K7QM-3XRB`.
5. Inicia sesión en [spectacast.com/account](/account/), abre tu organización y escribe el código en **Plan y PC** antes de una hora. El PC ya tiene su licencia y, si aún no tienes plan, su prueba.

Director se inicia ahora cada vez que inicias sesión en este PC. Sus archivos están en `C:\ProgramData\Spectacast\director`: el espectáculo en `shows\default.json`, los ajustes en `.env` y el registro en `logs\engine.log`.

## 2. Abrir el panel

Abre **http://127.0.0.1:4700** en un navegador de ese PC. El menú de idioma arriba a la derecha cambia entre English, Deutsch, Español e Italiano.

Para abrir el panel desde una tableta u otro PC, añade estas dos líneas a `C:\ProgramData\Spectacast\director\.env`, y luego cierra la sesión y vuelve a entrar:

```
HOST=0.0.0.0
PIN=<un PIN tuyo>
```

Sin PIN, Director no escucha en la red. Quien abre el panel escribe el PIN una vez. Para alguien que debe llevar el espectáculo sin cambiarlo, añade `OPERATOR_PIN=<otro PIN>`: abre solo los paneles.

## 3. Empezar con el espectáculo de ejemplo

1. En el menú del espectáculo, arriba, haz clic en **Ejemplo…**.
2. Elige el ejemplo con dos salas.
3. Confirma con **Usarlo**. Esto sustituye el espectáculo vacío.

El ejemplo tiene dos salas, Room A y Room B, cada una con Meet y OBS. También tiene una tira de canal por sala, el Wall con ambas pantallas y la regla que pone una sala al aire. Sus direcciones (192.168.1.11 y .12) son de ejemplo; las cambias en el paso siguiente.

## 4. Tu primera sala

En el PC de sala:

1. En OBS, abre **Herramientas > Configuración del servidor WebSocket**, activa el servidor, deja el puerto 4455 y pon una contraseña.
2. Inicia Spectacast Meet e inicia sesión con Zoom.

En el panel, en la página **Dispositivos**:

1. Haz clic en **buscar** en **Buscar en la red**. Director muestra los OBS y Meet que encuentra en la red.
2. Abre la tarjeta OBS de Room A y pon su dirección en `ws://<PC de sala>:4455`. Luego abre la tarjeta de la reunión de Room A y pon como host la dirección del PC de sala. Cada tarjeta se pone verde cuando el dispositivo responde.
3. Pon la contraseña de OBS en `.env` como `OBS_PASSWORD=<contraseña>`, y luego cierra la sesión y vuelve a entrar.
4. Si tienes una sola sala, quita los dos dispositivos de Room B, o déjalos: aparecen desconectados y no hacen nada.

## 5. Al aire

Abre **Paneles**. La tira de canal de Room A muestra su imagen, su reunión y si está al aire.

1. Inicia la reunión desde la tira.
2. Pulsa **on air**: OBS empieza a emitir a la dirección configurada en OBS.
3. Pulsa **on air** otra vez para parar.

En la prueba, dos salas pueden estar al aire 20 minutos seguidos, y las imágenes llevan una marca de prueba. A los 20 minutos las salas salen del aire; reinicia Director (cierra la sesión y vuelve a entrar) para probar otra vez.

{{shot:director-channels|Spectacast Director con cuatro salas una al lado de otra: quién está en cada reunión, la sala de espera, Preview y Program}}

## Lo siguiente

- **Más salas:** añade el OBS y el Meet de cada sala en **Dispositivos** y copia una tira de canal en **Paneles**.
- **Reglas:** en **Reglas**, cada regla dice qué la activa y qué hace, y muestra cuándo se ejecutó por última vez. Parte de las reglas del ejemplo y cámbialas.
- **Mic y Translator:** aparecen en **Dispositivos** como cualquier otro dispositivo. Consulta las guías de [Mic](/es/ayuda/mic/) y [Translator](/es/ayuda/translator/).

## Cuando algo no funciona

- **Una tarjeta sigue roja:** la dirección está mal, o el cortafuegos del PC de sala bloquea el puerto. Haz clic en la tarjeta para ver el último error.
- **«sin licencia para salir al aire»:** activa el PC (paso 1.5). La cabecera dice por qué no hay licencia.
- **Nada en http://127.0.0.1:4700:** mira `C:\ProgramData\Spectacast\director\logs\engine.log`.
- **Deshacer el ejemplo:** **Nuevo…** en el menú del espectáculo empieza uno vacío; **Exportar** guarda antes el que tienes.

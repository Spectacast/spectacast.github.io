# Reglas y scripts

<p class="lede">Una regla hace lo que de otro modo haría un operador a mano: cuando ocurre algo y se cumple una condición, ejecuta una lista de pasos. Gracias a las reglas, un solo operador puede seguir muchas salas.</p>

## Una regla tiene tres partes

1. **Disparador:** un evento de un dispositivo (alguien entra en la sala de espera), un valor del estado que cambia (un OBS empieza a emitir), un intervalo o **Solo al ejecutarla a mano**. Un disparador puede vigilar un dispositivo o todos los dispositivos de un driver, de modo que una regla sirve para todas las salas.
2. **Condición** (opcional): una expresión que debe cumplirse, como `obs.studioA.streaming`.
3. **Pasos:** los mismos pasos que ejecuta un botón. Consulta [Paneles](/es/ayuda/director-panels/).

En la página **Reglas**, **+ regla** empieza una regla vacía y **+ desde plantilla** construye una habitual con tus propios dispositivos, por ejemplo «quien habla pasa a una escena tras un tiempo de espera» o «una fuente NDI se cae, cambiar a una escena de reserva».

{{closeup:director-build-rule|Primer plano del editor de reglas de Director con la regla «Active speaker → Speaker»: cuando cambia quien habla en Zoom Sala A, tras un tiempo de espera de 1500 ms, OBS Sala A pone su escena|**Cuando**: lo que dispara la regla. Aquí, cambia quien habla en la Sala A.|**Solo si**: una condición y un tiempo de espera. Aquí, quien habla debe conservar la palabra un segundo y medio.|**Entonces**: lo que hace. Aquí, OBS de la Sala A cambia de escena.}}

## Tiempos y orden

- **tiempo de espera (ms):** la regla espera, y solo cuenta el último disparo de una ráfaga. Quien habla debe conservar la palabra un momento antes de que cambie la imagen.
- **pausa mínima (ms):** la regla no vuelve a ejecutarse durante ese tiempo.
- **prioridad:** cuando un evento coincide con varias reglas, la más alta se ejecuta primero.

## Probar antes de fiarse

- **simulación:** la regla anota lo que haría y no hace nada.
- **Ejecutar ahora** ejecuta una regla una vez sin esperar a su disparador. Su condición debe cumplirse igualmente.
- **Historial**, al final de la página, muestra cada ejecución y cada omisión con su motivo, y cada acción con su error.
- **Diagrama** dibuja todas las reglas: los disparadores a la izquierda, las reglas en el centro y, a la derecha, los dispositivos sobre los que actúan.

El interruptor **AUTOMATIZACIÓN ACTIVADA**, arriba en la página **Reglas**, pausa todas las reglas a la vez. Mientras están en pausa muestra **AUTOMATIZACIÓN DESACTIVADA**, y la cabecera muestra lo mismo en todas las páginas. Los botones y **Ejecutar ahora** siguen funcionando.

## Pasos de script

Para la lógica que los formularios no pueden expresar, un paso puede ser un fragmento corto de JavaScript. Se ejecuta en el PC de control y tiene a mano lo que necesita:

| Nombre | Qué es |
|---|---|
| `state` | Todo lo que Director sabe de cada dispositivo |
| `event` | Lo que disparó la regla |
| `vars` | Las variables |
| `setVar(id, value)` | Fija una variable |
| `await run(target, action, params)` | Ejecuta una acción en un dispositivo |
| `log(...)` | Escribe una línea en el registro de eventos |
| `await sleep(ms)` | Espera |

```
// Disparador: el evento "Entered the waiting room" de una reunión.
// Admitir a los ponentes al momento; los demás esperan al operador.
if (event.name.startsWith('Dr.')) {
  await run({ eventDevice: true }, 'admit', { by: 'zoomID', user: event.zoomId });
  log('admitted', event.name);
}
```

**Probar (simulación)** en el editor ejecuta el fragmento una vez sin tocar ningún dispositivo y muestra su registro. Un fragmento que falla, o que tarda más que su **tiempo límite (ms)** (cinco segundos si no lo cambias), cuenta como un paso fallido, y los pasos siguientes se ejecutan igualmente.

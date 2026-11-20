# Rules and scripts

<p class="lede">A rule does what an operator would otherwise do by hand: when something happens, and a condition holds, it runs a list of steps. Rules are what lets one operator follow many halls.</p>

## A rule has three parts

1. **Trigger:** an event of a device (someone enters the waiting room), a value in the state that changes (an OBS starts streaming), an interval, or **Only when run by hand**. A trigger can watch one device or every device of a driver, so one rule serves every hall.
2. **Condition** (optional): an expression that must hold, such as `obs.studioA.streaming`.
3. **Steps:** the same steps a button runs. See [Panels](/docs/director-panels/).

On the **Rules** page, **+ rule** starts an empty rule and **+ from template** builds a common one from your own devices, for example "the active speaker goes to a scene, after a hold time" or "an NDI source goes offline, switch to a fallback scene".

{{closeup:director-build-rule|Close-up of Director's rule editor with the rule "Active speaker → Speaker": when the active speaker changes in Zoom Hall A, after a hold time of 1500 ms, OBS Hall A sets its scene|**When**: what starts the rule. Here, the active speaker changes in Hall A.|**Only if**: a condition, and a hold time. Here, the speaker must keep the floor for a second and a half.|**Then**: what it does. Here, OBS in Hall A changes scene.}}

{{shot:director-rules|Director's rules page: each rule with what starts it and when it last ran}}

## Timing and order

- **hold time (ms):** the rule waits, and only the last trigger of a burst counts. A speaker must keep the floor for a moment before the picture changes.
- **cooldown (ms):** the rule does not run again for this long.
- **priority:** when one event matches several rules, the higher one runs first.

## Try before you trust

- **dry run:** the rule logs what it would do and does nothing.
- **Run now** runs a rule once without waiting for its trigger. Its condition must still hold.
- **History**, at the bottom of the page, lists every run and every skip with its reason, and each action with its error.
- **Graph** draws the whole rule set: triggers on the left, rules in the middle, the devices they touch on the right.

The **AUTOMATION ON** switch at the top of the **Rules** page pauses every rule at once. While they are paused it reads **AUTOMATION OFF**, and the header shows the same on every page. Buttons and **Run now** keep working.

## Script steps

For logic the forms cannot express, a step can be a short JavaScript snippet. It runs on the control-room PC and has what it needs in reach:

| Name | What it is |
|---|---|
| `state` | Everything Director knows about every device |
| `event` | What triggered the rule |
| `vars` | The variables |
| `setVar(id, value)` | Sets a variable |
| `await run(target, action, params)` | Runs an action on a device |
| `log(...)` | Writes a line to the event log |
| `await sleep(ms)` | Waits |

```
// Trigger: a meeting's event "Entered the waiting room".
// Admit the faculty at once; everyone else waits for the operator.
if (event.name.startsWith('Dr.')) {
  await run({ eventDevice: true }, 'admit', { by: 'zoomID', user: event.zoomId });
  log('admitted', event.name);
}
```

**Try (dry run)** in the editor runs the snippet once without touching any device and shows its log. A snippet that fails, or runs longer than its **timeout (ms)** (five seconds unless you change it), counts as one failed step, and the steps after it still run.

# Built to be extended

<p class="lede">Every venue has a device nobody planned for. Spectacast Director is made so that you can connect it yourself: describe its protocol on a form, script what the forms cannot say, and drive everything from your own systems through its API.</p>

{{cta}}

## Connect a device without code

On the Drivers page you describe a device's protocol: the commands it takes and the messages it sends back. Director speaks OSC, UDP, TCP, HTTP and WebSocket, which covers most lighting desks, audio mixers, video switchers and matrix routers. Once described, the device has buttons, live state and rules like the built-in ones.

You test against the real device, with every message in and out listed live, and you share a finished driver as one file.

[How to describe a driver →](/docs/director-drivers/)

{{closeup:director-build-driver|Close-up of Director's driver editor with the example "Generic OSC device": the transport OSC over UDP, the settings each device asks for, and the first commands|**How it talks**: OSC, UDP, TCP, HTTP or WebSocket.|**What each device needs**: here, two ports besides its address.|**Its commands**: each one becomes an action for buttons and rules.}}

## Rules, and scripts when rules are not enough

Rules react to what happens in the halls: someone enters the waiting room, a speaker takes the floor, a source goes offline. Most are built from forms. Where the logic is your own, a step can be a few lines of JavaScript with the whole state in reach.

{{closeup:director-build-rule|Close-up of Director's rule editor with the rule "Active speaker → Speaker": when the active speaker changes in Zoom Hall A, after a hold time of 1500 ms, OBS Hall A sets its scene|**When**: what starts the rule. Here, the active speaker changes in Hall A.|**Only if**: a condition, and a hold time. Here, the speaker must keep the floor for a second and a half.|**Then**: what it does. Here, OBS in Hall A changes scene.}}

[Rules and scripts →](/docs/director-rules/)

## An API for your own systems

Everything the dashboard does goes through an HTTP API on the control-room PC, and a WebSocket sends every change as it happens. A registration system, a show controller or a script can read the state of every hall, press a button, set a variable or run a rule, each with a token that limits what it may do.

[The API →](/docs/director-api/)

## Webhooks and OSC in

Another system starts something in Director with one call: a webhook over HTTP, or an OSC message. The programme of the congress can announce a session, and a rule puts the right title on the right hall.

## Stream Deck and MIDI

A Stream Deck key presses any control of the dashboard through Bitfocus Companion, with nothing extra to install. A MIDI control surface gives the operator real faders and keys, and rules can light them.

## Panels of your own

The dashboard's panels are yours to lay out: buttons, choices, text fields, level meters and live pictures, built once as a block and placed once per hall.

{{closeup:director-build-panel|Close-up of Director's panel editor: the row of ready-made blocks, the panel's grid with empty cells, and the Save button|**Blocks**: a whole hall, a meeting or a monitor, built once and placed wherever needed.|**Click an empty cell** to add a control or place a block, or a control to change it.|**Save**, and the panel is ready to use.}}

[Panels →](/docs/director-panels/)

## The device you need is not possible this way?

Some devices need their maker's own library. Those drivers are built into Director, like the ones for OBS Studio, NDI and Sennheiser EW-DX.

[Tell us what you want to control →](/contact/)

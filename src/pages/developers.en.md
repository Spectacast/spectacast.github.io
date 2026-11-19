# Built to be extended

<p class="lede">Every venue has a device nobody planned for. Spectacast Director is made so that you can connect it yourself: describe its protocol on a form, script what the forms cannot say, and drive everything from your own systems through its API.</p>

{{cta}}

## Connect a device without code

On the Drivers page you describe a device's protocol: the commands it takes and the messages it sends back. Director speaks OSC, UDP, TCP, HTTP and WebSocket, which covers most lighting desks, audio mixers, video switchers and matrix routers. Once described, the device has buttons, live state and rules like the built-in ones.

You test against the real device, with every message in and out listed live, and you share a finished driver as one file.

[How to describe a driver →](/docs/director-drivers/)

## Rules, and scripts when rules are not enough

Rules react to what happens in the halls: someone enters the waiting room, a speaker takes the floor, a source goes offline. Most are built from forms. Where the logic is your own, a step can be a few lines of JavaScript with the whole state in reach.

{{shot:director-rules|Director's rules page: each rule with what starts it and when it last ran}}

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

{{shot:director-panels|A Director panel with four halls: one block per hall, with its meeting, its waiting room, Preview and Program}}

[Panels →](/docs/director-panels/)

## The device you need is not possible this way?

Some devices need their maker's own library. Those drivers are built into Director, like the ones for OBS Studio, NDI and Sennheiser EW-DX.

[Tell us what you want to control →](/contact/)

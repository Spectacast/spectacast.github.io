# Your own driver

<p class="lede">The Drivers page describes a device's protocol without code. Once described, the device has actions, events and state like a built-in one, and panels and rules use it in the same way.</p>

A driver you define speaks one of five transports: **OSC**, **UDP**, **TCP**, **HTTP** or **WebSocket**. That covers most lighting desks, audio mixers, video switchers, matrix routers and building controls.

## 1. Start the driver

On the **Drivers** page click **+ driver over…** and pick the transport. Give the driver a name, then list the settings each device of it asks for: a host, a port, an API key. A setting has a default or is marked **req** (required), and the templates below read it as `config.<id>`.

## 2. Commands

Click **+ command** for each thing the device can be told. A command becomes an action that buttons and rules can run.

- Its **parameters** are typed fields, read in the message as `params.<id>`.
- Its **message** is a template. For OSC it is an address and typed arguments, such as `/cue/{{params.cue}}/go`. For HTTP it is a method, a path, headers and a body. For UDP, TCP and WebSocket it is a line of text, or bytes written in hex for a binary protocol.

## 3. Feedback

Click **+ feedback entry** for each message the device sends back. An entry recognises a message and says what to do with it.

- **Recognise** by an OSC address pattern (`/cue/{n}/active`, where `{n}` captures a part of the address), by a regular expression over text, or by an expression over a JSON message.
- **Set state:** write values from the message into the device's state, where panels show them and rules read them.
- **Raise an event** that a rule can react to.

An HTTP driver can also **poll**: it asks an address every few seconds and passes the answer through the same entries.

## 4. Online or offline

TCP and WebSocket devices are online while the connection is up, and Director reconnects by itself. UDP, OSC and HTTP devices need a **heartbeat**: a command sent at an interval whose answer shows the device is there. Without one they count as online.

## 5. Try it against the real device

Click **Create driver**, then add a device with your driver on the **Devices** page. Back on the **Drivers** page, click **try** on the driver's card, pick the device and click **trace messages**. Every message in and out is listed live, and each incoming one shows which feedback entries match it and what they would set. **Send test** runs a command with the parameters you type.

## 6. Share it

**export** downloads the definition as a JSON file; **import JSON** adds one to another show. The definitions are saved inside the show file, so a show carries its drivers with it.

Two examples to import and adapt: [a generic OSC device](/examples/drivers/generic-osc.json) and [an HTTP device whose status is polled](/examples/drivers/http-example.json).

## When this is not enough

A device that needs a vendor's own library, or a protocol these five transports cannot carry, needs a driver built into Director. [Tell us](/contact/) which device you want to control.

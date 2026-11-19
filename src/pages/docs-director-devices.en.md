# Devices and drivers

<p class="lede">Everything Director controls is a device: a hall's OBS, its meeting, a phone mic receiver, a wireless receiver, a MIDI controller. A driver tells Director what a kind of device can do and what it reports.</p>

## Add a device

1. Open the **Devices** page and go to the **Add device** form below the cards.
2. Pick the driver and type a name. The form shows one field for each setting the driver needs, with its default.
3. Click **Add**. The dot on the card turns green as soon as the device answers; the card shows its state and its last error.

**edit** on a card changes the name and the settings; Director reconnects when you save. **Scan the network**, then **scan**, lists every OBS and every Spectacast Meet that answers on the network; **use in the form** fills the form with one of them.

The OBS password stays out of the show file: put it in `C:\ProgramData\Spectacast\director\.env` as `OBS_PASSWORD=<password>`, then log off and on again. The password of a Sennheiser receiver or a Mic receiver is saved in the show file.

## The drivers that come with Director

| Driver | What Director sees and does |
|---|---|
| **OBS Studio** | Scenes, sources, audio, recording and streaming of an OBS, over its WebSocket server |
| **NDI discovery** | The NDI sources on the network, also through an NDI Discovery Server. A **Preview** control shows the picture of any of them |
| **Spectacast Meet** | Who is in the meeting and in the waiting room; admit, mute and spotlight; which feed goes to which output |
| **Spectacast Mic** | The phones connected to a hall PC as microphones and talkback |
| **Translator** | Start and stop a translation, choose the languages, read what was heard and what was said |
| **Sennheiser EW-DX receiver** | Each channel's mute, gain, level, radio link and battery. In Sennheiser Control Cockpit, switch on 3rd Party Access first (firmware 4.0.0 or newer) |
| **MIDI controller** | Notes and controllers in both directions: faders and buttons of a control surface |
| **Folder of files** | The clips in a folder, local or shared; a file copied in appears on its own |
| **Recorder** | Records a hall's meeting feed in hourly files |

A device that is not on this list gets a driver of its own on the **Drivers** page, without code: see [Your own driver](/docs/director-drivers/).

## Inputs from outside

Two inputs let another system start something in Director. Both are on the **Devices** page under **Inputs**.

- **Webhooks:** a call to `POST /api/hooks/<name>` raises the event `<name>`. The JSON body and the query string arrive as the event's fields.
- **OSC in:** set a port, and every OSC message that arrives on it becomes an event named after its address: `/cue/go` becomes `cue_go`.

A rule then reacts to the event. See [Rules and scripts](/docs/director-rules/) and [API, webhooks and Stream Deck](/docs/director-api/).

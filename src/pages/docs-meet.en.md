# Meet guide

<p class="lede">Spectacast Meet joins the online meeting from the hall PC and turns each participant, the gallery and each screen share into a video feed for the hall.</p>

## What you need

- A Windows PC in the hall, on the same network as the control room. A Mac works too, without interpretation channels.
- A Zoom account that can host the meeting.
- OBS Studio on the same PC, or a mixer that receives NDI.

## Install and sign in

1. Run Spectacast Setup on the hall PC and pick **Hall PC**. Setup installs what the hall PC runs, Meet among it, and shows a code to activate the PC as a hall PC under **Plan and PCs** in your account.
2. Start Meet. Its control panel opens in its own window; the tray icon brings it back.
3. Sign in with Zoom, and set the meeting the hall hosts under **Settings**: the meeting number, the name Meet shows in the meeting, and the microphone and speakers of the hall.

Meet starts again by itself after a restart of the PC, with the same settings and outputs.

## The control panel

| Tab | What it does |
| --- | --- |
| Meeting | start as host or join, leave or end, chat, mute everyone |
| Participants | mute, video, spotlight, hands, roles, rename, waiting room and breakout rooms, and a button per output to put someone on it |
| Outputs | how many feeds, and for each what it shows, at which resolution, with which sound |
| Settings | the meeting, the name, the audio devices, the Zoom sign-in, and the log |

## The feeds

Each output is an NDI source on the network. For each one, choose what it shows:

- **Participant:** one person, chosen by name.
- **Active speaker:** whoever spoke last.
- **Spotlight:** the spotlighted person, or a chosen person when nobody is.
- **Zoom view:** the meeting laid out the way Zoom does, without names or Zoom's graphics: the share while someone shares, otherwise the gallery or the speaker.

Then choose the picture (the camera, or the screen share when there is one) and the sound: that person's, the whole meeting, or the meeting without one person, for a return feed the room already hears. In OBS, add the feed as an NDI source.

## From the control room

In Director, Meet appears on **Devices** like any other device, and the channel strip on **Panels** shows who is in the meeting, who is talking and who is waiting. From there the operator admits people, mutes, and puts a speaker on an output, without touching the hall PC.

## Interpretation channels

When the meeting has interpretation, Meet can join as the interpreter of a language and speak with a voice from [Translator](/docs/translator/), or from a person in the booth. Listeners choose the language in Zoom as usual. Interpretation channels need Meet on Windows.

{{shot:meet-interpreter-card|The card Meet shows on an interpretation channel: the language and "Live interpretation"}}

## When something does not work

- **"Cannot connect to Zoom (no internet?)":** Meet keeps trying every minute; check the hall PC's internet.
- **An output is black:** nobody matches it, for example the chosen person has left. Pick another person, or set the output to Active speaker.
- **What Zoom answered:** the log is at the bottom of **Settings**.

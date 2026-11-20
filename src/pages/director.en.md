# Spectacast Director

<p class="lede">The control room for live hybrid events. One dashboard sees every hall PC, the online meeting and the microphones at once, and rules take care of what an operator would otherwise do by hand, many times a day.</p>

{{cta}}

{{loop:director-speaker|Pick a speaker, open the microphone, put them in the spotlight. Three touches.|Screen recording of Director: the operator picks Dr. Elena Ortega in Hall A, opens her microphone and puts her in the spotlight}}

## Every hall on one screen

Each hall gets its own strip: who is in the meeting and who is talking, the waiting room and the lobby, Preview and Program, the banner and the stream. Pick a speaker, put them on air with one touch, and the next hall is right beside it. One operator can follow a whole congress; at the 18-hall congress Director was built for, one did.

{{closeup:director-hall|Close-up of Hall A and Hall B in Director: both on air, the hall's PC and three speakers in each meeting with their microphone levels, and the waiting room|**Red means on air**, with the meeting and the mics.|**Who is in the meeting**, each with a live microphone level.|**The waiting room**: pick who is waiting, then Admit.}}

## Rules for the routine

Admit the faculty as they arrive, keep the waiting room as it was set, put a clip back where it was after a PC restarts, mute the hall when a video plays: rules react to what happens in the meeting, in OBS and on the mics, and do it the same way every time. Each rule shows when it last ran and why.

{{story:rule|Animation: Dr. Elena Ortega enters Hall A's waiting room, the rule "Auto admit" lights up, and she appears in the meeting}}

{{loop:director-clip|Put a clip on air: the hall's own microphone mutes by itself.|Screen recording of Director: the operator puts the clip on Program in Hall A, the hall turns to VOD and its microphone mutes; back on the meeting, it opens again}}

## Connectors, not a fixed setup

Director talks to each tool through a connector, so the video, the audio and the meeting platform are a choice:

- **OBS Studio**: scenes, sources, outputs and audio on every hall PC
- **NDI**: video and audio between PCs, with a multiview of every hall
- **Spectacast Meet, Mic and Translator**: the meeting as separate feeds, phones as microphones, live translation
- **Sennheiser EW-DX**: the hall's wireless mics, with levels and battery
- **MIDI and folders**: control surfaces, and the clips that appear during the show
- **Dante**: the hall's networked audio, through Dante Virtual Soundcard on a PC
- **Your own**: any device that speaks HTTP, OSC or plain sockets

How to connect a device of your own, script the rules and use the API: [Built to be extended](/developers/).

## Built for the hall

Director runs on a PC in the control room and talks to the hall PCs over the venue's own network, so a show keeps going when the internet does not. The fleet page lists every hall's PC, meeting and output at a glance; panels are built from blocks, so a new hall is one more copy, not a new design. The dashboard speaks English, German, Spanish and Italian.

{{closeup:director-fleet|Close-up of Director's fleet page: four halls, each online and in its meeting, with microphone levels and the waiting room|**Each hall's PC**: online, and in its meeting.|**Who is talking**: one bar per microphone, live.|**The waiting room**: admit everyone, or switch it on and off, from here.}}

{{plans:Director,Show,Complete}}

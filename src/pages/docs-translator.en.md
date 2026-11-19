# Translator guide

<p class="lede">Translator listens to a speaker and says what they say in another language, live, on any audio output. One Translator, called a lane, per language.</p>

## What you need

- A Windows PC in the hall or the control room, installed by Spectacast Setup and activated in your account.
- A plan with Translator: its minutes come with the PC's licence, with nothing to set up. Or your own Google Gemini or OpenAI key.
- An input with the speaker's voice: a microphone, the mixer, a phone through [Mic](/docs/mic/), or a feed over NDI.

## The control page

Each lane has its own control page, at **http://127.0.0.1:4720** for the first lane on that PC. Pick:

1. the **Microphone**, the input: a sound card, or an NDI source such as one participant from [Meet](/docs/meet/);
2. the **Output**: a sound card, a virtual cable into OBS or the mixer, or Meet's interpreter channel;
3. **Speak in**: the language to speak;

then press **Start**. The page shows each sentence twice, as heard and as said, while it is spoken.

{{shot:translator|The Translator control page: what was heard in Italian and what was said in English, line by line}}

## Engines

The engine decides how Translator sounds and how fast it answers. Google Gemini is the default; OpenAI is the other. The **interpreter** engines act as a congress interpreter: give them the session's **Topic** on the control page, and they also use a glossary of names and technical terms kept on the PC, one per line. We set up the glossary with you.

## Flagged meaning

While a lane runs, a second model reads what was heard beside what was said and flags in red the places where the translation says something different: a dropped "not", a number, left for right, a name. It changes nothing in what the lane says; it is for whoever watches the lane. The box **Warn when the meaning flips** turns it off.

## In the meeting

To give remote listeners a language in Zoom, set the lane's output to Meet's interpreter channel. Meet joins as that language's interpreter, and listeners pick the language in Zoom. See [Meet](/docs/meet/).

## After a restart

A lane remembers what it was doing. After a restart of the PC it comes back with the same input, output and language, and starts again if it was running, trying for ten minutes while a sound card or the network is not there yet.

## Minutes

Every minute a lane speaks counts, per language. Plans with Translator include {{INCLUDED_MINUTES}} minutes per hall; your account shows how many you have used. See [Account and billing](/docs/account-and-billing/).

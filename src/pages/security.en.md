# Security and data

<p class="lede">Most of Spectacast runs on your own computers, in the hall. This page says in plain words what stays there, what goes online and who handles it. The binding text is the <a href="{{PRIVACY_URL}}">Privacy Policy</a>.</p>

## What stays in the hall

Director, Meet and the Mic receiver are programs on your hall PCs. The video, the audio and the feeds of the meeting move between those PCs over the venue's own network, and recordings are files on your own disks. We do not receive any of it.

Phone mics are paired with the PC they talk to, and their audio is encrypted end to end on the way.

The online meeting itself is an ordinary Zoom meeting, held on your own Zoom account and under Zoom's terms.

## What goes online

| What | Where it goes | Why |
|---|---|---|
| **Licence check:** the PC's key, the identifier Windows gives the PC (we keep only a hash of it), the PC's name, the program version, and daily totals of use: minutes on air, Translator minutes per language, badges scanned | Our account server in the European Union | To check that your plan is active, how many PCs are in use and how many translation minutes were used |
| **Your account:** name, email, organisation, country, plan | Our account server in the European Union | To run your account and your licences |
| **Meet's Zoom sign-in:** your Zoom name and email, and the authorisation to host your meetings | Our server in the European Union | So that Meet can host the meeting on your Zoom account; removed when you disconnect Meet from Zoom |
| **Spectacast Pass:** attendees, badges, door scans, attendance | Our Pass server in the European Union | Pass is hosted by us for the event organiser |
| **Spectacast Translator:** the speech to translate | Google or OpenAI, whichever engine you choose for a language | The engine returns the translation live |
| **Translator's check for flipped meaning**, while it is switched on: the written transcript of the last minute | Google, or Anthropic when you set its key on the PC | To flag the places where the translation says something different from the speaker |
| **Payments** | Paddle, which sells Spectacast as Merchant of Record | Paddle takes the payment; we never see your card number |

The content of your event is never part of the licence check. This website sets no cookies and uses no analytics or advertising; signing in to your account or to Pass stores one sign-in cookie, which they need to work.

## When the internet drops

The halls and the control room keep working over the venue's own network, and a paid licence works for 14 days without the internet. The online meeting and the translation need the internet. The door phones of Pass keep deciding on their own and send their scans when the network is back.

## How the data is protected

- Every connection to our servers is encrypted (HTTPS).
- Passwords are stored only as salted hashes, never as text.
- The servers are in the European Union, with access limited to the people who run the service.
- The databases of Pass and of the accounts are backed up every night.
- Speech sent to Translator's engines travels over an encrypted connection, and under their API terms neither Google nor OpenAI uses it to train its general models.

## Who handles data for us

| Provider | What for | Where |
|---|---|---|
| **Hetzner Online GmbH** | Hosting of Pass, the account and licence server and this website | European Union |
| **Google (Gemini API) and OpenAI (Realtime API)** | Speech translation, when you use the minutes included in your plan | May be outside the European Union, including the United States |
| **Brevo (Sendinblue SAS)** | Sending the emails of your account and the badges that Pass emails to attendees | France |
| **Porkbun, LLC** | Forwarding email sent to our spectacast.com addresses | United States |

Paddle is not on this list because it handles your payment details as a controller in its own right. When you use Translator with your own Google or OpenAI key, you contract with the engine directly and we receive nothing.

## Your attendees' data

For the people at your event, you are the controller and we are your processor (art. 28 GDPR). We handle their data only on your instructions. We send the data processing agreement on request: write to [privacy@spectacast.com](mailto:privacy@spectacast.com).

How long each kind of data is kept is listed in the [Privacy Policy]({{PRIVACY_URL}}).

## Reporting a security problem

If you find a weakness in Spectacast, write to [support@spectacast.com](mailto:support@spectacast.com) before you make it public, so that we can fix it first.

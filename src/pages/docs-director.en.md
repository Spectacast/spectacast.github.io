# Director guide

<p class="lede">From a new control-room PC to your first hall on air in about half an hour.</p>

You need a Windows 10 or 11 PC for the control room and, for each hall, a Windows PC with OBS Studio and Spectacast Meet. All the PCs must be on the same network.

## 1. Install on the control-room PC

1. Download Spectacast Setup from [Downloads](/downloads/) and unzip it.
2. Double-click **Setup.cmd**. Windows asks for administrator rights.
3. Pick **1, Control room**.
4. Setup installs Director, opens its firewall ports and starts it. It then shows a code such as `K7QM-3XRB`.
5. Sign in at [spectacast.com/account](/account/), open your organisation and type the code under **Plan and PCs** within an hour. The PC now has its licence, and its trial if you have no plan yet.

Director now starts every time you log on to this PC. Its files are in `C:\ProgramData\Spectacast\director`: the show in `shows\default.json`, the settings in `.env` and the log in `logs\engine.log`.

## 2. Open the dashboard

Open **http://127.0.0.1:4700** in a browser on that PC. The language menu at the top right switches between English, Deutsch, Español and Italiano.

To open the dashboard from a tablet or another PC, add these two lines to `C:\ProgramData\Spectacast\director\.env`, then log off and on again:

```
HOST=0.0.0.0
PIN=<a PIN of your own>
```

Director refuses to listen on the network without a PIN. Whoever opens the dashboard types the PIN once. For someone who should run the show without changing it, add `OPERATOR_PIN=<another PIN>`: that opens the panels only.

## 3. Start from the example show

1. In the show menu at the top, click **Example…**.
2. Pick the example with two rooms.
3. Confirm with **Use it**. This replaces the empty show.

The example has two halls, Room A and Room B, each with Meet and OBS. It also has a channel strip per hall, the Wall with both screens, and the rule that puts a hall on air. Its addresses (192.168.1.11 and .12) are placeholders, which you change in the next step.

## 4. Your first hall

On the hall PC:

1. In OBS, open **Tools > WebSocket Server Settings**, turn the server on, keep port 4455 and set a password.
2. Start Spectacast Meet and sign in with Zoom.

On the dashboard, on the **Devices** page:

1. Click **scan** under **Scan the network**. Director lists the OBS and Meet it finds on the network.
2. Open the OBS card of Room A and set its address to `ws://<hall PC>:4455`. Then open the meeting card of Room A and set its host to the hall PC's address. Each card turns green once the device answers.
3. Put the OBS password in `.env` as `OBS_PASSWORD=<password>`, then log off and on again.
4. If you have one hall, remove Room B's two devices, or leave them: they show as offline and do nothing.

## 5. On air

Open **Panels**. Room A's channel strip shows its picture, its meeting and its on-air state.

1. Start the meeting from the strip.
2. Press **on air**: OBS starts streaming to the address set in OBS.
3. Press **on air** again to stop.

In the trial, two halls can be on air for 20 minutes per run, and the pictures carry a trial mark. After 20 minutes the halls go off air; restart Director (log off and on) to try again.

{{shot:director-channels|Director with four halls side by side: who is in each meeting, the waiting room, Preview and Program}}

## Next

- **More halls:** add each hall's OBS and Meet on **Devices**, then copy a channel strip on **Panels**.
- **Rules:** on **Rules**, each rule says what starts it and what it does, and shows when it last ran. Start from the example's rules and change them.
- **Mic and Translator:** they appear on **Devices** like any other device. See the [Mic](/docs/mic/) and [Translator](/docs/translator/) guides.

## When something does not work

- **A card stays red:** the address is wrong, or the hall PC's firewall blocks the port. Click the card to see the last error.
- **"no licence to go on air":** activate the PC (step 1.5). The header says why there is no licence.
- **Nothing on http://127.0.0.1:4700:** look at `C:\ProgramData\Spectacast\director\logs\engine.log`.
- **Undo the example:** **New…** in the show menu starts an empty show; **Export** saves the one you have first.

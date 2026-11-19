# Pass guide

<p class="lede">Set up an event in Pass, turn phones into door scanners, and get the attendance afterwards. Pass runs in the browser, at spectacast.com/pass.</p>

## 1. The event

Sign in at [spectacast.com/pass](/pass/) with your Spectacast account and create a **New event**. Then, under **Setup**:

- **Zones:** the halls and rooms where presence is counted.
- **Doors:** one per entrance, each in a zone.
- **Sessions:** the program. Mark with **Counts** the sessions that count towards attendance.
- **Categories:** the kinds of attendees, such as Faculty, Delegate or Staff.

The checklist at the top says what is still missing.

## 2. Attendees and badges

Under **Attendees**:

- **+ Person** adds one by hand, for example someone who registers at the desk.
- **Import** reads a CSV, or Excel saved as CSV, with headers such as First name, Last name, Email, Category and ID (Italian and German headers work too). Other columns are kept as fields that rules and messages can use. Importing again updates the same people.
- **Feeds** pull the list from a registration site by themselves, and **Keys for other systems** let a site push its registrations. Ask your registration site's provider, or us, to connect them.

Each attendee gets a badge with a QR code. **Print all badges** prints them, on your own background if you upload one, or **Email badges** sends each person theirs.

## 3. The doors

At each door, use a phone or tablet, or a keyboard scanner plugged into a laptop.

1. Under **Setup**, **Doors**, press **Set up a phone** for the door.
2. Point the phone's camera at the QR code on the screen and open the link. The door app opens on that door, with nothing to type.
3. Add it to the home screen, so it opens like an app.

The door answers each badge at once, full-screen in green, amber or red, with a sound and the person's name. When the network drops, the door keeps deciding by itself and sends its scans when the network is back.

{{phone:pass-door-welcome|The door app on a phone: a green screen with "Welcome Sofia"}}

A **keyboard scanner** works on the same door page: set it to send Enter after each code. A scanner in storage mode, at a door without a screen, is read out later under **Upload scans**.

## 4. Rules

What a door says is decided by **Rules**, tried from the top; the first that matches decides. A new event starts with sensible ones: ignore a double read, refuse unknown or cancelled badges, warn when someone is already inside, refuse a full room, welcome everyone else. Add your own, for example a room for one category only, and try any badge with **Test a scan** before the doors open.

## 5. During the event

**Live** shows how many people are in each room, the latest scans, the door phones and whether they are online. Anything a door decided while offline differently from the server is listed under **To review**.

## 6. Afterwards

**Reports** give, per person, the minutes and the percentage spent in each session, ready for Excel. Under **Certificates**, set what a person needs for a certificate of attendance; those who meet it download theirs.

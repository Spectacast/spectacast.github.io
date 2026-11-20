# Panels

<p class="lede">A panel is a page of controls that you lay out yourself: buttons, switches, choices, text fields and the tiles of each hall. The example show's panels are a starting point, and every one can be changed.</p>

{{shot:director-panels|A Director panel with four halls: one block per hall, with its meeting, its waiting room, Preview and Program}}

## Edit a panel

On the **Panels** page click **Edit**. Now a click on an empty cell adds a control, and a click on a control opens its properties.

- Select several controls with Shift-click or by dragging a rectangle, then move, copy or delete them together.
- **Undo** and **Redo** go back and forward up to a hundred steps.
- **Save** keeps the changes for every dashboard; **Discard** drops them.

**+ panel** adds a page. An operator who signs in with the operator PIN sees the panels and nothing else.

{{closeup:director-build-panel|Close-up of Director's panel editor: the row of ready-made blocks, the panel's grid with empty cells, and the Save button|**Blocks**: a whole hall, a meeting or a monitor, built once and placed wherever needed.|**Click an empty cell** to add a control or place a block, or a control to change it.|**Save**, and the panel is ready to use.}}

## Controls

| Control | What it does |
|---|---|
| **Button** | Runs its steps when pressed |
| **Toggle** | A switch: one list of steps to turn on, one to turn off |
| **Select (choices)** | A row of choices: a fixed list, or a live one such as an OBS's scenes or the people in a meeting |
| **Text entry** | A field with a Set button, for a banner line or a name |
| **Label** | Shows a text or a value |
| **Device status** | Shows whether a device is connected |
| **Preview (picture of a device)** | The live picture of an OBS or an NDI source |
| **Mixer (audio inputs of a device)** | Faders and mute for a device's audio inputs |
| **Frame (group)** | A titled border around controls that belong together |
| **Block** | A set of controls built once and placed many times |

## What a press does

A press runs a list of steps, from the top:

- an **action** on a device, such as "switch the program scene";
- a **delay**;
- **setting a variable**;
- an **if** with a list for yes and a list for no;
- steps that run **in parallel**, or once **for each** item of a list.

**Ask first** makes the dashboard ask a question before it runs the steps, for the buttons that should not be pressed by accident.

## Feedback: how a control looks

**Feedback** entries change a control's colour and text from the live state: red while a hall is on air, a name when someone is in the waiting room. The entries are tried from the top and the first one that holds wins.

## Blocks: one strip for every hall

Build the controls of one hall once, select them and click **Make block**. The devices they name become the block's **Values**. Place the block once per hall and give each placement its own devices. A change to the block reaches every hall at once.

## Variables

The **Variables** page holds values that panels and rules share: the clip that was picked, the speaker who has the floor. **Add variable** makes one, with its type and the value it starts with.

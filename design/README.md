# Spectacast design system: Paper

One style file, one token file and the fonts, shared by every Spectacast module
(Pass, Program, Translator, Mic, Meet, Director). Open `guide.html` for the one-page brand guide
with every component in light, dark and console.

| file | what |
|---|---|
| `spectacast.css` | tokens (`--sc-*`), base (`class="sc"`), components (`sc-btn`, `sc-badge`, `sc-table`, `sc-tile`, `sc-dialog`, forms, tabs, chips, meter) |
| `tokens.json` | the same values for native code (Mic Android/iOS, Meet and Mic desktop) |
| `fonts/` | Inter, Inter Tight, JetBrains Mono (latin + latin-ext, variable, SIL OFL) |
| `guide.html` | brand guide and component sheet |
| `sync.sh` | copies the files into a module |

## Use it

```sh
./design/sync.sh ../pass/web/static/design   # any folder the module serves
```

```html
<html class="sc">
<link rel="stylesheet" href="/static/design/spectacast.css">
```

Modules **copy** the files (never link to spectacast.com): hall PCs run without internet and a
change here must not reach a live show until the module ships it. Change the design here,
bump `VERSION`, then sync each module in its own PR.

Theme follows the system; `<html data-theme="light|dark">` forces one. Director panels add
`data-surface="console"` (always dark, one step deeper).

## Rules (from the brand spec)

- Red (`--sc-live`) only for on air, recording, "you are live". Problems are ink with an icon.
- Every status has a word or an icon; colour is extra.
- Selected = ink fill. Director Preview = 2px ink outline; Program live = red fill.
- No layout shift: mode-dependent controls keep their space (`visibility: hidden`).
- Compact cards, fixed column widths, row actions on hover.
- Director panel layout changes only with Liviu's OK; colours, type and components may change.

Light `ok`, `warn` and `live` are one shade darker than the first mock-ups so small text passes
WCAG AA on paper and white (`#2a6f46`, `#8a5208`, `#cf2e25`). Red fills with white text use
`--sc-live-fill` (`#cf2e25`) in every theme.

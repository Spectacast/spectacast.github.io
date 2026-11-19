# spectacast.com

The Spectacast website, served by GitHub Pages with the custom domain in `CNAME` (the server behind
spectacast.com copies `main` every 10 minutes).

## Changing a page

The pages are generated: edit the sources in [src/](src/), never the `index.html` files.

```sh
pip install markdown pillow
python3 src/build.py --check
```

- `src/home.html`: the English home page body; its German, Spanish and Italian texts are in
  `src/home_texts.py` and the build stops on an English text without them.
- `src/pages/<page>.<lang>.md`: pricing, terms, refunds, privacy and the product pages (director, meet,
  mic, translator, pass), one file per language. Product pages take `{{shot:name|alt text}}` (a
  screenshot from `img/screens/`, in the page's language or in light and dark when those exist),
  `{{phone:name|alt}}`, `{{plans:Director,Show}}` and `{{cta}}`.
- `tools/screenshots/run.sh ../pass ../director ../translator ../meet`: retakes the screenshots from the apps' own code with an invented
  Demo Congress 2027 (see the comments in each script).
- `src/content.py`: seller details, plans, prices and VAT.
- `src/build.py`: the shared header and footer, the page list, and `LAUNCHED`, which shows the sign-in,
  free trial and download buttons only from the 1.0 launch.

Every page exists in English, German, Spanish and Italian. `--check` fails on a missing language, a broken
link or a missing anchor, and CI also fails when the committed pages differ from what the sources build.

The logo files are in [brand/](brand/): `mark.svg` (square, also the GitHub avatar as
`avatar-1024.png`), `mark-line.svg` (the S alone, in the text colour), and the word mark for
light (`lockup-dark`) and dark (`lockup-light`) backgrounds. The SVG word marks use the system
Helvetica, so share the PNGs when the font matters.

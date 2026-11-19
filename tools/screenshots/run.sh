#!/bin/sh
# Retakes the website's screenshots from the apps' own code, with the invented Demo Congress 2027,
# and writes them as WebP to img/screens/. Run from the website repository, with the app repositories
# checked out next to it (npm install done in pass and director):
#   sh tools/screenshots/run.sh ../pass ../director ../translator
set -e
PASS=${1:?pass repo}; DIRECTOR=${2:?director repo}; TRANSLATOR=${3:?translator repo}
RAW=$(mktemp -d)
node tools/screenshots/shot-pass.js "$PASS" "$RAW"
node tools/screenshots/shot-director.js "$DIRECTOR" "$RAW"
node tools/screenshots/shot-translator.js "$TRANSLATOR" "$RAW"
mkdir -p img/screens
python3 - "$RAW" img/screens <<'PY'
import sys, pathlib
from PIL import Image
src, dst = map(pathlib.Path, sys.argv[1:])
for f in sorted(src.glob('*.png')):
    im = Image.open(f).convert('RGB')
    if im.width > 1600:  # the phone shots are taken at 2x; keep them sharp but not huge
        im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
    im.save(dst / (f.stem + '.webp'), 'WEBP', quality=86, method=6)
    print('img/screens/' + f.stem + '.webp')
PY
rm -rf "$RAW"

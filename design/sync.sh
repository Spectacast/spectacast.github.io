#!/usr/bin/env sh
# Copy the Spectacast design system into a module: ./design/sync.sh <target-folder>
# The target gets spectacast.css, tokens.json, VERSION and fonts/. Commit them in the module.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
target=${1:?usage: sync.sh <target-folder>}
mkdir -p "$target/fonts"
cp "$here/spectacast.css" "$here/tokens.json" "$here/VERSION" "$target/"
cp "$here"/fonts/*.woff2 "$here"/fonts/OFL-*.txt "$target/fonts/"
echo "Spectacast design $(cat "$here/VERSION") -> $target"

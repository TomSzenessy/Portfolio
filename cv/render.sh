#!/bin/sh
# Build cv-*.html from build.py, then render each to a one-page A4 PDF with headless Chrome.
# Usage: ./render.sh   (outputs Tom_Szenessy_CV_<LANG>.pdf next to this script)
cd "$(dirname "$0")" || exit 1
python3 build.py || exit 1
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in cv-*.html; do
  lang=$(echo "${f#cv-}" | cut -d. -f1 | tr '[:lower:]' '[:upper:]')
  out="Tom_Szenessy_CV_${lang}.pdf"
  "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --allow-file-access-from-files \
    --virtual-time-budget=4000 --print-to-pdf="$PWD/$out" "file://$PWD/$f" 2>/dev/null
  pages=$(pdfinfo "$out" | awk '/^Pages:/{print $2}')
  echo "$out: $pages page(s)"
  [ "$pages" = "1" ] || echo "  WARNING: content overflows one page"
done

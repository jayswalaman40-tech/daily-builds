#!/usr/bin/env bash
# Publishes one pre-staged tool live: moves _pending/<slug> -> <slug>, adds its
# landing card to index.html, commits and pushes. Usage: bash _pending/promote.sh <slug>
SLUG="$1"
git fetch origin -q && git checkout -B main origin/main -q
if [ -f "$SLUG/index.html" ]; then echo "already-live: $SLUG"; exit 0; fi
git mv "_pending/$SLUG" "$SLUG"
python3 - "$SLUG" <<'PYEOF'
import sys
slug=sys.argv[1]
h=open('index.html',encoding='utf-8').read()
if slug not in h:
    card=open('_pending/'+slug+'.card.html',encoding='utf-8').read()
    i=h.find('tool-card soon'); j=h.rfind('<div',0,i)
    h=h[:j]+card+h[j:]
    open('index.html','w',encoding='utf-8').write(h)
    print('card inserted')
PYEOF
git rm -q "_pending/$SLUG.card.html" 2>/dev/null || true
git add -A
git commit -q -m "Launch pre-staged tool: $SLUG"
git push origin HEAD:main && echo PUSHED

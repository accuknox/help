#!/bin/bash
# usage: fc.sh <url> <outname>
KEY=$(python "D:\Atharva\NOTES\SCRIPTS\keys\keys.py" firecrawl 2>/dev/null)
curl -s -X POST https://api.firecrawl.dev/v2/scrape -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
  -d "{\"url\":\"$1\",\"formats\":[\"markdown\"],\"onlyMainContent\":false}" | python -c "import sys,json;d=json.load(sys.stdin);print(d.get('data',{}).get('markdown') or d)" > "$2.md"
wc -c "$2.md"

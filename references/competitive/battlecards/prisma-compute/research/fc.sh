#!/bin/bash
# usage: fc.sh <url>   writes raw/<slug>.md
KEY=$(python "D:\Atharva\NOTES\SCRIPTS\keys\keys.py" firecrawl 2>/dev/null)
slug=$(echo "$1" | sed -E 's#https://docs.prismacloud.io/##; s#[/]#__#g')
curl -s -X POST https://api.firecrawl.dev/v2/scrape -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
  -d "{\"url\":\"$1\",\"formats\":[\"markdown\"],\"onlyMainContent\":true}" | python -c "import sys,json;d=json.load(sys.stdin);print(d.get('data',{}).get('markdown') or 'FAILED '+str(d)[:200])" > "raw/$slug.md"

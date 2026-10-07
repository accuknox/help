#!/bin/bash
# usage: fc2.sh <keyslot> <url>   retries on rate limit
slot=$1; url=$2
KEY=$(grep -E "^FIRECRAWL_API_KEY_$slot=" "D:/Atharva/NOTES/.env" | cut -d= -f2- | tr -d '"\r ')
slug=$(echo "$url" | sed -E 's#https://docs.prismacloud.io/##; s#[/]#__#g')
for i in 1 2 3 4; do
  out=$(curl -s -X POST https://api.firecrawl.dev/v2/scrape -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
   -d "{\"url\":\"$url\",\"formats\":[\"markdown\"],\"onlyMainContent\":true}" | python -c "import sys,json;d=json.load(sys.stdin);print(d.get('data',{}).get('markdown') or 'FAILED '+str(d)[:200])")
  case "$out" in FAILED*) sleep 25;; *) echo "$out" > "raw/$slug.md"; exit 0;; esac
done
echo "$out" > "raw/$slug.md"

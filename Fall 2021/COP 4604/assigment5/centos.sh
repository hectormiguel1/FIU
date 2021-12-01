#!/bin/bash

csv=$(curl -s http://users.cis.fiu.edu/~ggome002/files/hrami024.csv)
zodiacs=($(echo "$csv" | awk -F "\"*,\"*" '{print $8}' | sort -u))
audit_file='/root/audit.txt'
http_audit_file="/etc/httpd/logs/access_log"

for zodiac in "${zodiacs[@]}"; do
    instances=($(cat "$http_audit_file" | grep "$zodiac" | awk '{print $1}'))
    echo "$zodiac" "${#instances[@]}" 
    echo "$zodiac" "${#instances[@]}" > "$audit_file"
done
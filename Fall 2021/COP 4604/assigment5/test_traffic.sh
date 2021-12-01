#!/bin/bash
csv=$(curl -s http://users.cis.fiu.edu/~ggome002/files/hrami024.csv)
zodiacs=($(echo "$csv" | awk -F "\"*,\"*" '{print $8}' | sort -u))
size=${#zodiacs[@]}

for item in {0..1000}; do
    curl localhost/zodiac/"${zodiacs[$((RANDOM%size))]}"
done

    
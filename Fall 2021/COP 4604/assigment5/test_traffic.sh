#!/bin/bash
csv=$(curl -s http://users.cis.fiu.edu/~ggome002/files/{USERNAME}.csv)
zodiacs=($(echo "$csv" | awk -F "\"*,\"*" '{print $8}' | sort -u))
size=${#zodiacs[@]}

for item in {0..1000}; do
    curl localhost/zodiac/"${zodiacs[$((RANDOM%size))]}"
done

    
#!/bin/bash

PORT=8075
#installs Socat
yum install socat -y -q > /dev/null 2> /dev/null
file="hrami024.csv"

while IFS= read -r line
do
    echo "$line" | socat - TCP4-LISTEN:$PORT
    PORT=$((PORT + 1))
done < $file
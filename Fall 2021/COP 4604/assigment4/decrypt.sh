#!/bin/bash

words=($(cat words.txt))

TRUE=1
FALSE=0
ERROR=1

# Function will attempt to decript using passed word as the password
function decrypt() {
    output_buffer=$(openssl enc -aes-256-cbc -d -in redacted.csv -pass pass:"$1" 2> /dev/null )
    if [ $? -ge $ERROR ]; then echo $FALSE; else echo $TRUE; echo $output_buffer > decrypted.csv; fi
}

for word in "${words[@]}"
    do
        result=$(decrypt "$word")
        if [ "$result" -eq $TRUE ]; then echo "$word"; exit 0; fi
    done
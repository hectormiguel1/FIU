#!/bin/bash

words=($(cat /root/dictionary))
character=$1

for word in "${words[@]}"
    do
        wordInitial=${word:0:1}
        if [ "$character" == "$wordInitial" ];
         then
            word_revered=$(echo "$word" | rev)
            if [ "$word" == "$word_revered" ]; 
                then 
                    echo "$word" >> output
                fi 
         fi
    done
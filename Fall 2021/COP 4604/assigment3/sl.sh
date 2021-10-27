#!/bin/bash

data=$(curl -s http://users.cis.fiu.edu/~ggome002/files/hrami024.csv)
usernames=($(echo "$data" | awk -F "\"*,\"*" '{print $1}'))
first_names=($(echo "$data" | awk -F "\"*,\"*" '{print $2}'))
dinos=($(echo "$data" | awk -F "\"*,\"*" '{print $12}'))
tv_generas=($(echo "$data" | awk -F "\"*,\"*" '{print $11}'))
len=${#usernames[*]}

for letter in {a..z} 
do
    for ((index=0; index < len; index++))
    do
        if [ -d "/home/${letter}/${usernames[index]}" ]
        then
            file_dino=$(cat /home/"${letter}"/"${usernames[index]}"/dino)
            file_tv_genera=$(cat /home/"${letter}"/"${usernames[index]}"/dino)

            if [ "$file_dino" != "${dinos[index]}" ] ||
               [ "$file_tv_genera" != "${tv_generas[index]}" ];
            then
                echo "${usernames[index]}" >> /root/output.txt
            fi
        fi
    done
done
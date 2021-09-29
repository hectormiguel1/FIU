#!/bin/bash

data=$(curl -s http://users.cis.fiu.edu/~ggome002/files/hrami024.csv)

lastnames=($(echo "$data" | awk -F "\"*,\"*" '{print $3}'))
usernames=($(echo "$data" | awk -F "\"*,\"*" '{print $1}'))
planets=($(echo "$data" | awk -F "\"*,\"*" '{print $10}'))
zodiacs=($(echo "$data" | awk -F "\"*,\"*" '{print $8}' ))
len=${#usernames[*]}

echo "usernames Array Length: ${len}"
#echo "Usernames: ${usernames[*]}"

for letter in {a..z} 
do 
    echo "Creating folder: /home/${letter}"
    mkdir /home/"${letter}"
    for ((i = 1; i < len; i++))
    do 
        username=${usernames[i]}
        lastname=${lastnames[i]}
        planet=${planets[i]}
        zodiac=${zodiacs[i]}
        firstLetter=${lastname:0:1}
        if [ "$letter" == "$firstLetter" ];
            then
                echo "Letter: $letter, First Letter: $firstLetter"
                echo "Creating user $username because lastname: $lastname starts with $letter"
                mkdir /home/"$letter"/"$username"
                echo "${planet} > /home/$letter/$username/planet"
                echo "${zodiac} > /home/$letter/$username/zodiac"
                echo "$planet" > /home/"$letter"/"$username"/planet
                echo "$zodiac" > /home/"$letter"/"$username"/zodiac
        fi
    done 
done 
#!/bin/bash

#Setup constants
DATE=$1
SECONDS_PER_DAY=86400
TRUE=1
FALSE=0
ERROR=1

#Function will validate that the passed date is valid
function isDateValid() {
    date -d "$1" 2> /dev/null > /dev/null

    if [ $? -ge $ERROR ]; then echo $FALSE; else echo $TRUE; fi
}

#Function will compute the days between today and the provided date.
function computeDays() {
    diffrence=$(( ($(date +%s --date "$1") - $(date +%s) )/ SECONDS_PER_DAY ))
    echo "$diffrence"
}

#function converts a date in DDMMYYYY format to YYYYMMDD format
function reformatDate() {
    # Convert incoming number to a string
    date=$(printf '%d' "$1")
    #Separate sections to create the date in the new format.
    day=${date:0:2}
    month=${date:2:2}
    year=${date:4:4}
    echo "$year$month$day"

}
#Function will provide the 2 letter day from the date
function getDay() {
    day=$(date --date "$1" +%a )
    echo "${day:0:2}"
}

isValid=$(isDateValid "$DATE")

if [ "$isValid" -eq $FALSE ];
    then
        echo "Date: $DATE, is not valid reformatting to YYYYMMDD"
        DATE=$(reformatDate "$DATE");
        echo "Date Reformatted: $DATE"
fi

DAYS=$(computeDays "$DATE");
DAY_STR=$(getDay "$DATE");

if [ "$DAYS" -lt 0 ];
            then
                echo "$DATE was ${DAYS#-} Days ago";
                echo "$DATE landed on a $DAY_STR";
        else
            echo "$DAYS Days until $DATE"
            echo "$DATE lands on a $DAY_STR"
        fi
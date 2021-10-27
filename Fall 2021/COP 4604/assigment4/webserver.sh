#!/bin/bash

server=$1

#Set up boolean values and constants
FALSE=0
TRUE=1
ERROR=1

#Get user csv from server
curl http://users.cis.fiu.edu/~ggome002/files/hrami024.csv > hrami024.csv

#Extract odd, event and lines multople of 7
ODDS=$(awk 'NR %2 == 1' hrami024.csv)
EVEN=$(awk 'NR %2 == 0' hrami024.csv)
MULTIPLE_OF_SEVEN=$(awk 'NR %7 == 0' hrami024.csv)

function isInstalled() {
    which "$1" > /dev/null 2>&1

    case $? in
        0) echo $TRUE;;
        *) echo $FALSE;;
    esac
}

function installServer() {
    yum install -y -q $server
    if [ $? -ge $ERROR ];
        then
            echo "Error Encountered installing $server, make sure it is available in your ditro repos"
    fi
}

function init() {
    local installed=$(isInstalled httpd);
    local counter=0
    local max_attempts=5
    while [ $installed -ne $TRUE ]
        do
            if [ $counter -ge $max_attempts ]; then break; fi
            installServer
            local installed=$(isInstalled $server)
            local counter=$(( counter + 1 ))
        done
    if [ $installed -eq $FALSE ];
        then
            echo "Unable to install $server, terminating...";
            exit $ERROR;
    fi
    #Clean whatever is currently in index.html
    > /var/www/html/index.html

    case $server in
        httpd)
            echo $ODDS > /var/www/html/index.html
        ;;
        nginx)
            echo $EVEN > /var/www/html/index.html
            ;;
        lighttpd)
            echo $MULTIPLE_OF_SEVEN > /var/www/html/index.html
            ;;
        esac

    #Stopping Services
    systemctl stop httpd.service
    systemctl stop lighttpd.service 
    systemctl stop nginx.service

    #Start server
    systemctl start "$server.service"

}

case $server in
    httpd | lighttpd | nginx)
        init;
        ;;
    *)
        echo 'Invalid entry';
        ;;
esac;


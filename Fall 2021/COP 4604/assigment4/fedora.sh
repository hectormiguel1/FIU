#!/bin/bash

if [ $# -eq 0 ]; then echo "No arguments passed"; exit; fi 

if [ "$1" -le 0 ];
    then
        echo "Unable to run fibonacci sequence with numbers of 0 or less"
    else
        count=$(($1 - 2))
        fib1=0
        fib2=1
        if [ $1 -ge 1 ]; then echo -n $fib1; fi
        if [ $1 -ge 2 ]; then echo -n ", $fib2"; fi
        for _ in $(seq 1 "$count");
        do
            fib3=$((fib1 + fib2))
            fib1=$fib2
            fib2=$fib3
            echo -n ", $fib3"
        done 
fi
echo ""
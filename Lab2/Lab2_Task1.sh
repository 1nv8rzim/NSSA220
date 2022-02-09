#!/bin/bash

usage () {
    echo "Usage: Lab2_Task1.sh num_rands [min] [max]"
    echo "num_rands int: number of random numbers"
    echo "min       int: lowest random number"
    echo "max       int: highest random number"
}

isNum () {
    if ! [ "$1" -eq "$1" ] 2>/dev/null; then
        echo "Error: $1 is not an integer"
        usage
        exit 1
    fi
}

if [ $# -lt 1 ]; then
    echo "Error: Must have at least 1 parameter"
    usage
    exit 1
fi

if [ $# -gt 3 ]; then
    echo "Error: Must have at most 3 parameter"
    usage
    exit 1
fi

if [ $1 == "-h" ]; then
    usage
    exit 0
fi

isNum $1

if [ $# -eq 3 ]; then
    isNum $2
    isNum $3
fi

if [ $# -eq 2 ]; then
    isNum $2
fi


num_rands=$1
min=$2
max=$3

echo $num_rands
echo $min
echo $max
#!/bin/bash

usage () {
    echo "Usage: Lab2_Task1.sh num_rands [min] [max]"
    echo "num_rands int: number of random numbers"
    echo "min       int: lowest random number"
    echo "max       int: highest random number"
}

is_num () {
    if ! [ "$1" -eq "$1" ] 2>/dev/null; then
        echo "Error: $1 is not an integer"
        usage
        exit 1
    fi
}

num_writer () {
    echo $2 >> "rands_${1}.txt"
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

is_num $1

if [ $# -eq 3 ]; then
    is_num $1
    is_num $2
    is_num $3
    
    num_rands=$1
    min=$2
    max=$3
    
    echo "You requested ${num_rands} numbers between ${min} and ${max}"
    
fi

if [ $# -eq 2 ]; then
    is_num $1
    is_num $2
    
    num_rands=$1
    min=$2
    max=32767
    
    echo "You requested ${num_rands} numbers greater than ${min}"
    
fi

if [ $# -eq 1 ]; then
    is_num $1
    
    num_rands=$1
    min=1
    max=32767
    
    echo "You requested ${num_rands} numbers"
fi

rm "rands_${num_rands}.txt" 2>/dev/null

total=0

for i in $(seq $num_rands); do
    num=$(( $RANDOM % $(( max - min + 1 )) + min))
    num_writer $num_rands $num
    total=$((total + num))
done

minimum=$(sort -n "rands_${num_rands}.txt" | head -1)
echo "The smallest value generated was ${minimum}"
maximum=$(sort -rn "rands_${num_rands}.txt" | head -1)
echo "The largest value generated was ${maximum}"
average=$((total / num_rands))
echo "The average value generated was $average"

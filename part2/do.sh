#!/bin/bash

if [[ -e "$1".class ]]; then
    rm "$1".class
fi

if [[ "$2" = '-o' ]]; then
    if [ ! -d out ]; then
        mkdir out/
    fi

    if [[ -z "$3" ]]; then
        javac "$1".java > out/"$1".txt
        java $1 > out/"$1".txt
    else
        javac "$1".java > out/"$3".txt
        java $1 > out/"$3".txt
    fi
else
    javac "$1".java
    java $1
fi

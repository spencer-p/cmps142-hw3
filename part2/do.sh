#!/bin/bash

CLASS=""

if [[ "$1" = "LR" ]]; then
    CLASS="LogisticRegression"
elif [[ "$1" = "LRB" ]]; then
    CLASS="LogisticRegression_withBias"
elif [[ "$1" = "LRR" ]]; then
    CLASS="LogisticRegression_withRegularization"
else
    CLASS="$1"
fi

if [[ -e "$CLASS".class ]]; then
    rm "$CLASS".class
fi

if [[ "$2" = '-o' ]]; then
    if [ ! -d out ]; then
        mkdir out/
    fi

    if [[ -z "$3" ]]; then
        javac cmps142_hw4/"$CLASS".java > out/"$CLASS".txt
        java cmps142_hw4.$CLASS > out/"$CLASS".txt
    else
        javac cmps142_hw4/"$CLASS".java > out/"$3".txt
        java cmps142_hw4.$CLASS > out/"$3".txt
    fi
else
    javac cmps142_hw4/"$CLASS".java
    java cmps142_hw4.$CLASS
fi

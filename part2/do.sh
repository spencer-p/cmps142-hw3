#!/bin/bash

if [ ! -d out ]; then
    mkdir out/
fi

javac "$1".java
java $1 > out/"$1".txt

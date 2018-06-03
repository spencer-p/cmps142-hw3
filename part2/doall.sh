#!/bin/bash

if [[ "$1" = "-o" ]]; then
    rm cmps142_hw4/*.class

    if [ -d out ]; then
        rm -rf out/
    fi

    mkdir out/

    source do.sh LogisticRegression -o
    source do.sh LogisticRegression_withBias -o
    source do.sh LogisticRegression_withRegularization -o
else
    source do.sh LogisticRegression
    source do.sh LogisticRegression_withBias
    source do.sh LogisticRegression_withRegularization
fi

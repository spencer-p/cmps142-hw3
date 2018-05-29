#!/bin/bash

rm -rf out/
mkdir out/

source do.sh LogisticRegression > out/LogisticRegression.txt
source do.sh LogisticRegression_withBias > out/LogisticRegression_withBias.txt
source do.sh LogisticRegression_withRegularization > out/LogisticRegression_withRegularization.txt

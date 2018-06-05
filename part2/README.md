# CMPS 142 HW3 - Java

Please note that all the java files are in the directory `cmps142_hw4` since
they define their package to be `cmps142_hw4`. Use the shell scripts (below) to
compile and run.

# Setting up

* Install JDK

# Running

* To compile a class: `javac <class>.java`. (note it has extension)
* To run the class: `java <class>`. (note no extension here)

I made a script that does both for a class (no extension needed)...
```bash
./do.sh <class>
```
* Possible abreviations to use as values for `<class>` are:
    - `LR` for LogisticRegression
    - `LRB` for LogisticRegression_withBias
    - `LRR` for LogisticRegression_withRegularization

It is possible to save data to a file with `-o` flag:
```bash
./do.sh <class> -o [<file>]
```
Note `<file>` is optional. If ont specified defaulst to the name of the class. In any case, it's saved to `/out`.

Also another script does it for all three files and  optionally pipes the output to files in `out/`:
```bash
./doall.sh [-o]
```

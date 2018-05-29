# CMPS 142 HW3 - JAva

# Setting up

* Install JDK

# Running

* To compile a class: `javac <class>.java`. (note it has extension)
* To run the class: `java <class>`. (note no extension here)

I made a script that does both for a class (no extension needed)...
```bash
./do.sh <class>
```

Also another script does it for all three files and pipes the output to files in `out/`:
```bash
./doall.sh
```
For this, errors still show in the console, not in the file (easier to debug?).

# CMPS 142 HW3 - Python

I tried to make sure the correct stuff gets downloaded when `main.py` is run.

# Setting up

Optionally you can create a virtualenv:

```bash
virtualenv .
source bin/activate
```

And then install required packages:

```bash
pip install -r requirements.txt
```

# Running

The program is run with the following command:

```bash
python2 main.py [-h] [-d DATA_DIR] [-s SAVE_DIR] [-t] [-e]
```

Note that `python2 main.py` is usually enough because:
* `DATA_DIR` defaults to data/. (expected to have *train_file_cmps142_hw3* and *test_file_cmps142_hw3*)
* `SAVE_DIR` defaults to out/. (if it doesn't exists it's automatically created)
* `-t` shows the output (question answering) for the train set.
* `-e` shows the output (question answering) for the test set.
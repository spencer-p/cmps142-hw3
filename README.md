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
python2 main.py [-h] [-d DATA_FILE] [-s SAVE_DIR]
```

Note that `python2 main.py` is usually enough because:
* `DATA_FILE` defaults to data/train_file_cmps142_hw3.
* `SAVE_DIR` defaults to out/. (if it doesn't exists it's automatically created)

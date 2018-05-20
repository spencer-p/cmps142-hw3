# CMPS 142 HW3 - Python

I tried to make sure the correct stuff gets downloaded when `main.py` is run.

# Running

Currently it's only in a pre-processing stage.

Optionally you can create a virtualenv:

```bash
virtualenv .
source bin/activate
```

On my system it's actually `virtualenv2` for the Python 2 virtualenv.

Anyway, then to actually run the thing:

```bash
pip install -r requirements.txt
python main.py PATH_TO_TRAIN_DATA_HERE
```

And then hopefully it should (think for a few seconds, and then) print out all
the preprocessed data. Again, it might be `python2` to run it with Python 2.

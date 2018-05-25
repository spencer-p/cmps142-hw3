"""
main.py
"""

import sys
import pprint
import nltk
import os
import io
import argparse

from nltk.probability import FreqDist
from preprocess import preprocess

TRAIN_FILE = "train_file_cmps142_hw3"
TEST_FILE = "test_file_cmps142_hw3"

def setup_unicode():
    # Do the utf-8 thing
    reload(sys)
    sys.setdefaultencoding('utf-8')


def setup_nltk():
    # Make nltk use the current directory for storing files
    # instead of polluting the home directory
    #
    nltk.data.path.insert(0, os.getcwd())
    # Make sure the corpus (corpi?) are downloaded
    if not os.path.isdir('tokenizers/punkt'):
        nltk.download('punkt', os.getcwd())

    if not os.path.isdir('corpora/stopwords'):
        nltk.download('stopwords', os.getcwd())


def check_dir(directory, create=True):
    # Checks that it's a directory and exists. Returns the path with the '/'
    # at the end
    d = directory
    if d[-1] != '/':
        d = d + '/'
    if not os.path.exists(d):
        if create:
            try:
                os.makedirs(d)
                return d
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        else:
            return False

    return d

def save(filename, texts, freqdist, labels):
    # Step 7.a: Save preprocessed file
    headers = list(freqdist.keys())
    lines = []

    # Build lines
    for i in range(0, len(texts)):
        values = []
        # Get the freq of that line
        f = FreqDist(texts[i])

        # Check all words and append value for that word or 0
        for w in freqdist:
            if w in f:
                values.append(u'{}'.format(f[w]))
            else:
                values.append(u'0')

        # Append the label
        lines.append(values + [labels[i]])

    headers = headers + [u'Label']

    # Write to file
    with io.open(filename, 'w', encoding='utf8') as outfile:
        l = ','.join(headers) + '\n'
        outfile.write(l)

        for line in lines:
            l = ','.join(line) + '\n'
            outfile.write(l)

        outfile.close()

def process_file(dir_read, dir_save, filename, useFreq=None):
    fname = dir_save + filename + '_prep.csv'

    # Read data file
    with io.open(dir_read + filename, 'r', encoding='utf8') as infile:
        input_text = infile.read()
        infile.close()

    # Preprocess file
    processed_texts, freq, labels = preprocess(input_text)

    # Save
    if useFreq is not None:
        f = useFreq
    else:
        f = freq
    save(fname, processed_texts, f, labels)

    # Give the frequency and the file back
    return f, fname


def main(_data_dir, _save_dir):
    # Setup stuff
    setup_unicode()
    setup_nltk()

    # Check directories are ok
    data_dir = check_dir(_data_dir, create=False)
    if data_dir is False:
        raise Exception("Directory " + _data_dir + " not present.")

    save_dir = check_dir(_save_dir)

    # Do processing
    train_freq, train_file = process_file(data_dir, save_dir, TRAIN_FILE)
    test_freq, test_file = process_file(data_dir, save_dir, TEST_FILE, useFreq=train_freq)

    return train_file, test_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Homework 3 - Part 1')
    parser.add_argument('-d', '--data', dest='data_dir', default='data/',
                        help='Data dir to use for training/test.')
    parser.add_argument('-s', '--save', dest='save_dir',
                        default='out/', help='Directory to save outputs to.')

    args = parser.parse_args()

    train_file, test_file = main(args.data_dir, args.save_dir)

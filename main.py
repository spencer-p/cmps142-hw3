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


def check_dir(directory):
    # Checks that it's a directory and exists. Returns the path with the '/'
    # at the end
    d = directory
    if d[-1] != '/':
        d = d + '/'
    if not os.path.exists(d):
        try:
            os.makedirs(d)
            return d
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    return d


def main(data_file, save_dir):
    setup_unicode()
    setup_nltk()

    # Read data file
    with io.open(data_file, 'r', encoding='utf8') as infile:
        input_text = infile.read()
        infile.close()

    # Preprocess data file
    processed_texts, freq, labels = preprocess(input_text)
    # pprint.pprint(processed_texts[0])

    save = check_dir(save_dir)

    # Step 7.a: Save preprocessed file
    headers = list(freq.keys())
    lines = []

    for i in range(0, len(processed_texts)):
        values = []
        # Get the freq of that line
        f = FreqDist(processed_texts[i])

        # Check all words and append value for that word or 0
        for w in freq:
            if w in f:
                values.append(u'{}'.format(f[w]))
            else:
                values.append(u'0')

        # Append the label
        lines.append(values + [labels[i]])

    headers = headers + [u'Label']

    with io.open(save + data_file.split('/')[-1] + '_prep.csv', 'w', encoding='utf8') as outfile:
        l = ','.join(headers) + '\n'
        outfile.write(l)

        for line in lines:
            l = ','.join(line) + '\n'
            outfile.write(l)

        outfile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Homework 3 - Part 1')
    parser.add_argument('-d', '--data', dest='data_file', default='data/train_file_cmps142_hw3',
                        help='Data file to use for training/classification.')
    parser.add_argument('-s', '--save', dest='save_dir',
                        default='out/', help='Directory to save outputs to.')

    args = parser.parse_args()

    main(args.data_file, args.save_dir)

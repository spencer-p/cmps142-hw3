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


def save(filename, texts, freqdist, labels, output_train=False, output_test=False):
    # Step 7.a: Save preprocessed file
    headers = list(freqdist.keys())
    lines = []

    if output_train:
        if 'yellow' in freqdist:
            answer_question('STEP 7.b', 'Yes, the frequency contains "yellow".')
        else:
            answer_question('STEP 7.b', 'No, the frequency doesn\'t contain "yellow".')
        if 'music' in freqdist:
            answer_question('STEP 7.c', 'Yes, the frequency contains "music".')
        else:
            answer_question('STEP 7.c', 'No, the frequency doesn\'t contain "music".')

    # Build lines
    for i in range(0, len(texts)):
        values = []
        # Get the freq of that line
        f = FreqDist(texts[i])

        # Check all words and append value for that word or 0
        for w in freqdist:
            if w in f:
                values.append(f[w])
            else:
                values.append(0)

        s = sum(values)
        if i == 0 and output_train:
            answer_question('STEP 7.d', 'The sum of the second row is ' + str(s) + '.')

        values = [u'{}'.format(str(v)) for v in values]
        # Append the label
        lines.append(values + [labels[i]])

    if output_train:
        zero_sums = 0
        for i in range(0, len(headers) - 1):
            col = [int(l[i]) for l in lines]
            if sum(col) == 0:
                zero_sums = zero_sums + 1
        answer_question('STEP 7.e', 'There are ' + str(zero_sums) + ' columns that sum to 0.')

    headers = headers + [u'Label']

    if output_test:
        answer_question('STEP 2.b', 'Total number of rows (including headers) is ' + str(len(lines) + 1) + '.')
        answer_question('STEP 2.c', 'Total number of columns (including label) is ' + str(len(headers)) + '.')
        answer_question('STEP 2.d', 'First 5 columns headers for both files are ' + str(headers[:5]) + '.')

        if u'head' in headers:
            answer_question('STEP 2.e', 'Yes, the headers contain "head".')
        else:
            answer_question('STEP 2.e', 'Yes, the headers don\'t contain "head".')

        zero_sums = 0
        for i in range(0, len(headers) - 1):
            col = [int(l[i]) for l in lines]
            if sum(col) == 0:
                zero_sums = zero_sums + 1
        answer_question('STEP 2.f', 'There are ' + str(zero_sums) + ' columns that sum to 0.')

    # Write to file
    with io.open(filename, 'w', encoding='utf8') as outfile:
        l = ','.join(headers) + '\n'
        outfile.write(l)

        for line in lines:
            l = ','.join(line) + '\n'
            outfile.write(l)


def process_file(dir_read, dir_save, filename, useFreq=None, output_train=False, output_test=False):
    fname = dir_save + filename + '_prep.csv'

    # Read data file
    with io.open(dir_read + filename, 'r', encoding='utf8') as infile:
        input_text = infile.read()

    # Preprocess file
    processed_texts, freq, labels = preprocess(input_text, output_train=output_train, output_test=output_test)

    # Save
    if useFreq is not None:
        f = useFreq
    else:
        f = freq
    save(fname, processed_texts, f, labels, output_train=output_train, output_test=output_test)

    # Give the frequency and the file back
    return f, fname


def answer_question(q, t):
    s = '[{}] {}'.format(q, t)
    print(s)


def main(_data_dir, _save_dir, output_train=False, output_test=False):
    # Setup stuff
    setup_unicode()
    setup_nltk()

    # Check directories are ok
    data_dir = check_dir(_data_dir, create=False)
    if data_dir is False:
        raise Exception("Directory " + _data_dir + " not present.")

    save_dir = check_dir(_save_dir)

    # Do processing
    print('### Processing Training set ###')
    train_freq, train_file = process_file(
        data_dir, save_dir, TRAIN_FILE, output_train=output_train)
    if output_train:
        print('')
    print('### Processing Testing  set ###')
    test_freq, test_file = process_file(
        data_dir, save_dir, TEST_FILE, useFreq=train_freq, output_test=output_test)
    if output_train:
        print('')
    print('###          Done.          ###')

    return train_file, test_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Homework 3 - Part 1')
    parser.add_argument('-d', '--data', dest='data_dir', default='data/',
                        help='Data dir to use for training/test.')
    parser.add_argument('-s', '--save', dest='save_dir',
                        default='out/', help='Directory to save outputs to.')
    parser.add_argument('-t', '--output-train', dest='out_train', default=False,
                        help='Print training output.', action='store_true')
    parser.add_argument('-e', '--output-test', dest='out_test', default=False,
                        help='Print training output.', action='store_true')

    args = parser.parse_args()

    train_file, test_file = main(args.data_dir, args.save_dir, args.out_train, args.out_test)

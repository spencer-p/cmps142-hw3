"""
main.py
"""

import sys
import pprint
import nltk
import os
import io

from preprocess import preprocess

if __name__ == '__main__':
    # Do the utf-8 thing
    reload(sys)
    sys.setdefaultencoding('utf-8')

    # Make nltk use the current directory for storing files
    # instead of polluting the home directory
    nltk.data.path.insert(0, os.getcwd())

    # Make sure the corpus (corpi?) are downloaded
    if not os.path.isdir('tokenizers/punkt'):
        nltk.download('punkt', os.getcwd())

    if not os.path.isdir('corpora/stopwords'):
        nltk.download('stopwords', os.getcwd())

    # Preprocess that data
    # Note use of io.open to get unicode data, not straight ascii bytes
    with io.open(sys.argv[1], 'r', encoding='utf8') as infile:
        input_text = infile.read()
        processed_texts = preprocess(input_text)
        pprint.pprint(processed_texts)


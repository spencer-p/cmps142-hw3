"""
preprocess.py

Preprocesses text data.
"""

from nltk import word_tokenize
from nltk.corpus import stopwords as sw
from nltk.stem.porter import PorterStemmer
import unicodedata
import sys
import string

# Removing punctuation from unicde is tricky
# I'm doing this because the word_tokenizer gives us unicode, so we want
# everything to be unicode
# Anyway, use this punctuation table with unicode.translate()
# https://stackoverflow.com/questions/11066400/remove-punctuation-from-unicode-formatted-strings#11066687
# punctuation = dict.fromkeys(i for i in xrange(sys.maxunicode)
#         if unicodedata.category(unichr(i)).startswith('P'))

stopwords = set(sw.words('english'))
punctuation = [i for i in u'{}'.format(string.punctuation)]

def preprocess(s):
    """
    preprocess takes a string of the form
    '(ham|spam) words words words\n(ham|spam) more words here....'
    And returns a list of processed texts. The class is removed, all words are
    lowercase, there are no stop words or punctuation, all the words are
    stemmed, and tokens that appear less than 5 times in the entire string are
    removed entirely.
    """
    # Step 1: Remove uppercase, and make utf-8 to be sure
    s = s.lower()

    # Step 2: Tokenize!
    # Split everything by line (one line for each text)
    # Tokenize it
    # Skip word 1 (the class -- spam/ham)
    # Also trim the last item (it's an empty string after the last \n)
    texts = [word_tokenize(text)[1:] for text in s.split('\n')][:-1]

    # Step 3: Remove stop words
    # Step 4: Remove punctuation
    # Step 5: Stem all the tokens
    # Doing this all in one go for simplicity.
    stemmer = PorterStemmer()
    for i in range(len(texts)):
        texts[i] = [stemmer.stem(word.translate(punctuation))
                for word in texts[i] if word not in stopwords
                and word not in punctuation]

    # tokens = []
    # for text in texts:
    #     tokens = tokens + text

    # Compute word frequency so we can dump words used < 5 times
    freq = {}
    for text in texts:
        for word in text:
            if word not in freq: freq[word] = 0
            freq[word] += 1

    # Step 6: Dump all infrequent tokens
    for i in range(len(texts)):
        texts[i] = [word for word in texts[i] if freq[word] >= 5]

    # Done!
    return texts

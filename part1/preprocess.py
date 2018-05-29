"""
preprocess.py

Preprocesses text data.
"""

from nltk import word_tokenize
from nltk.corpus import stopwords as sw
from nltk.probability import FreqDist
from nltk.stem.porter import PorterStemmer
import unicodedata
import sys
import string


def preprocess(s, output_train=False, output_test=False):
    """
    preprocess takes a string of the form
    '(ham|spam) words words words\n(ham|spam) more words here....'
    And returns a list of processed texts. The class is removed, all words are
    lowercase, there are no stop words or punctuation, all the words are
    stemmed, and tokens that appear less than 5 times in the entire string are
    removed entirely.
    Return values:
     - list of processed SMS texts
     - nltk.probability.FreqDist of frequency of tokens
     - labels of each SMS text in order
    """

    # Removing punctuation from unicde is tricky
    # I'm doing this because the word_tokenizer gives us unicode, so we want
    # everything to be unicode
    # Anyway, use this punctuation table with unicode.translate()
    # https://stackoverflow.com/questions/11066400/remove-punctuation-from-unicode-formatted-strings#11066687
    # punctuation = dict.fromkeys(i for i in xrange(sys.maxunicode)
    #         if unicodedata.category(unichr(i)).startswith('P'))

    stopwords = set(sw.words('english'))
    punctuation = [i for i in u'{}'.format(string.punctuation)]

    # Step 1: Remove uppercase, and make utf-8 to be sure
    s = s.lower()

    # Step 2: Tokenize!
    # Split everything by line (one line for each text)
    # Tokenize it
    # Skip word 1 (the class -- spam/ham), put it to array
    # Also trim the last item (it's an empty string after the last \n)
    token_texts = [word_tokenize(text) for text in s.split('\n')][:-1]
    labels = [text[0] for text in token_texts]

    texts = [text[1:] for text in token_texts]

    if output_train:
        answer_question('STEP 2.a', 'Total numner of distinct tokens is ' +
                        str(FreqDist([word for text in texts for word in text]).B()) + '.')

    # Step 3: Remove stop words
    # Step 4: Remove punctuation
    # Step 5: Stem all the tokens
    # Doing this all in one go for simplicity.
    stemmer = PorterStemmer()
    for i in range(len(texts)):
        texts[i] = [stemmer.stem(word) for word in texts[i]
                    if word not in stopwords
                    and word not in punctuation]

    if output_train:
        answer_question('STEP 5.a', 'The list is ' + str(texts[10]) + '.')
    if output_test:
        answer_question('STEP 1.a', 'The list is ' + str(texts[23]) + '.')

    # Get freq distribution of the whole set
    freq = FreqDist([word for text in texts for word in text])

    # Step 6: Dump all infrequent tokens
    # Note that len(freq) can give you the number of unique tokens in the data
    texts = [[word for word in text if freq[word] >= 5] for text in texts]
    freq = FreqDist([word for text in texts for word in text])

    if output_train:
        answer_question(
            'STEP 6.a', 'Total numner of distinct tokens is ' + str(freq.B()) + '.')

    # Done!
    return texts, freq, labels


def answer_question(q, t):
    s = '[{}] {}'.format(q, t)
    print(s)

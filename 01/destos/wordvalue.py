import operator

from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dict_fp:
        return dict_fp.read().splitlines()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES.get(letter.upper(), 0) for letter in word])

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()

    word_values = {word: calc_word_value(word) for word in words}
    return max(word_values.items(), key=operator.itemgetter(1))[0]


if __name__ == "__main__":
    pass # run unittests to validate

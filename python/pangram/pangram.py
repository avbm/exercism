import string


def is_pangram(sentence):
    for letter in string.ascii_lowercase:
        if letter not in sentence and letter.upper() not in sentence:
            return False
    else:
        return True

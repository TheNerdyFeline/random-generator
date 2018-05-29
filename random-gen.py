import random
import string
import RandomWords


def random_string(num):
    """(number) -> string

    return a random string the length of the number input"""
    new_string = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation)
                          for n in range(num)])
    return new_string


def random_words(num):
    """(number) -> string

    return a string of x number of random words, x = num"""
    return 0
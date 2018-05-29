import random
import string
from random_words import RandomWords
rw = RandomWords()


def random_string(num):
    """(number) -> string

    return a random string the length of the number input"""
    new_string = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation)
                          for n in range(num)])
    return new_string


def random_words(num):
    """(number) -> array

    return an array of x number of random words, x = num"""
    new_pw = rw.random_words(count=num)
    return new_pw

import time
from test import test_me

# Given two strings, write a method to decide if one is a permutation of the other
def check_permutation_sort(string_a: str, string_b):
    if len(string_a) != len(string_b):
        return False
    return sorted(string_a) == sorted(string_b)


def check_permutation_count(string_a: str, string_b):
    # assumption: ASCII alphabet
    # O(n + 128)

    if len(string_a) != len(string_b):
        return False
    store = {}
    for i in range(len(string_a)):
        letter_a = string_a[i]
        letter_b = string_b[i]
        if letter_a not in store:
            store[letter_a] = 1
        else:
            store[letter_a] += 1

        if letter_b not in store:
            store[letter_b] = -1
        else:
            store[letter_b] -= 1

    for v in store.values():
        if v != 0:
            return False
    return True


def check_permutation_count_b(string_a: str, string_b):
    # assumption: ASCII alphabet
    # O(2n)

    if len(string_a) != len(string_b):
        return False

    store = {}

    for letter in string_a:
        if letter not in store:
            store[letter] = 1
        else:
            store[letter] += 1

    for letter in string_b:
        if letter not in store:
            return False

        store[letter] -= 1

        if store[letter] < 0:
            return False

    return True


test_cases = [
    {"i": ("dog", "god"), "o": True},
    {"i": ("abcd", "bacd"), "o": True},
    {"i": ("3563476", "7334566"), "o": True},
    {"i": ("wef34f", "wffe34"), "o": True},
    {"i": ("dogx", "godz"), "o": False},
    {"i": ("abcd", "d2cba"), "o": False},
    {"i": ("2354", "1234"), "o": False},
    {"i": ("dcw4f", "dcw5f"), "o": False},
    {"i": ("DOG", "dog"), "o": False},
    {"i": ("dog ", "dog"), "o": False},
    {"i": ("aaab", "bbba"), "o": False},
]

test_functions = [
    check_permutation_sort,
    check_permutation_count,
    check_permutation_count_b,
]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

import time
from test import test_me


def is_unique_dict(input_string: str):
    if len(input_string) == 0:
        return True
    table = {}
    for letter in input_string:
        if letter not in table:
            table[letter] = 1
        else:
            return False
    return True


def is_unique_algorithmic(input_string: str):
    # assumption: characters come from the ASCII alphabet

    if len(input_string) > 128:
        return False

    table = [False] * 128
    for letter in input_string:
        value = ord(letter)
        if table[value]:
            return False
        table[value] = True
    return True


test_cases = [
    {"i": "", "o": True},
    {"i": "a", "o": True},
    {"i": "ba", "o": True},
    {"i": "aaa", "o": False},
    {"i": "aab", "o": False},
    {"i": "baa", "o": False},
    {"i": "baaab", "o": False},
    {"i": "abc", "o": True},
    {"i": "23ds2", "o": False},
    {"i": "hb 627jh=j ()", "o": False},
    {"i": "".join([chr(val) for val in range(128)]), "o": True},
    {"i": "".join([chr(val // 2) for val in range(129)]), "o": False},
]

test_functions = [is_unique_dict, is_unique_algorithmic]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

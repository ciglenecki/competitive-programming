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
    ["", True],
    ["a", True],
    ["ba", True],
    ["aaa", False],
    ["aab", False],
    ["baa", False],
    ["baaab", False],
    ["abc", True],
    ("23ds2", False),
    ("hb 627jh=j ()", False),
    ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
    ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
]

test_functions = [is_unique_dict, is_unique_algorithmic]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

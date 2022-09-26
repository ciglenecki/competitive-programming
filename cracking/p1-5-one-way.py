from test import test_me

"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE
pale,ple-> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def is_one_way_edit(str_a: str, str_b: str) -> bool:
    if len(str_a) >= len(str_b):
        bigger = str_a
        smaller = str_b

    if len(bigger) > len(smaller) + 1:
        return False

    if len(smaller) == 0:
        return True

    si = 0
    diff = False
    for bi in range(len(bigger)):
        if si >= len(smaller):
            return True

        if diff and smaller[si - 1] != bigger[bi] and smaller[si] != bigger[bi]:
            return False

        elif smaller[si] != bigger[bi]:
            diff = True

        si += 1
    return True


test_cases = [
    {"i": ("pale", "ple"), "o": True},
    {"i": ("pales", "pale"), "o": True},
    {"i": ("pale", "bale"), "o": True},
    {"i": ("pale", "bake"), "o": False},
]

test_functions = [
    is_one_way_edit,
]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

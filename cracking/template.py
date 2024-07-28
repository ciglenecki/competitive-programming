from __future__ import annotations

from tests.test import Case, test_me


def solution(arg):
    return None


test_cases: list[Case] = [
    {
        "i": "input",
        "o": [1, 2, 3],
    }
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

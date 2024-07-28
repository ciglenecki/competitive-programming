from __future__ import annotations

from cracking.crack_3_1_stack import Multistack
from tests.test import Case, test_me


class Stack:
    def __init__(self) -> None:
        self.items = []
        self.min = None

    @staticmethod
    def from_list(items: list):
        stack = Stack()
        stack.items = items
        return stack

    def pop(self):
        self.items.pop(-1)
        if item < self.min:
            self.min = item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def push(self, item):
        self.items.append(item)
        if item < self.min:
            self.min = item

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


def solution(ms: Multistack):
    ms.push(0, 1)
    ms.push(1, 1)
    ms.push(2, 1)

    result = []
    return ms.items
    for s, stack_items in enumerate(ms.items):
        for item in stack_items:
            result.append(item)
    return result


test_cases: list[Case] = [
    {
        "i": (
            Multistack.from_list(
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                ],
                stack_size=4,
            ),
        ),
        "o": [1, 2, 3, 1, 4, 5, 6, 1, 7, 8, 9, 1],
    }
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

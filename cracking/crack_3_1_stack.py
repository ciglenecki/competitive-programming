from __future__ import annotations

from ast import Mult

from tests.test import Case, test_me

"""

0 1 2 3 4 | 0 1 2 3 4 | 0 1 2 3 4

"""


class Multistack:
    def __init__(self, num_stacks: int, stack_size: int) -> None:
        self.items = [None] * (num_stacks * stack_size)
        self.stack_size = stack_size
        self.num_stacks = num_stacks
        self.sizes = [0] * num_stacks

    @staticmethod
    def from_list(items: list[list], stack_size: int = 5):
        stack = Multistack(len(items), stack_size)
        for stack_num, stack_items in enumerate(items):
            for item in stack_items:
                stack.push(stack_num, item)
        return stack

    def index_of_top(self, num_stack):
        offset = num_stack * self.stack_size
        return offset + self.sizes[num_stack]

    def pop(self, stack_num: int):
        self._assert_valid_stack_num(stack_num)
        i = self.index_of_top(stack_num)

        value = self.items[i]
        self.items[i] = None
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return None
        i = self.index_of_top(stack_num)
        return self.items[i]

    def push(self, stack_num: int, item):
        print("push")
        self._assert_valid_stack_num(stack_num)
        if self.is_full(stack_num):
            raise Exception(f"Stack {stack_num} full")
        i = self.index_of_top(stack_num)

        print(i, self.items, item)
        self.items[i] = item
        self.sizes[stack_num] += 1

    def is_empty(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == self.stack_size

    def __len__(self):
        return len(self.items)

    def _assert_valid_stack_num(self, stack_num):
        if stack_num >= self.num_stacks:
            raise Exception(f"Stack #{stack_num} does not exist")


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

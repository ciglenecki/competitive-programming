from __future__ import annotations

import random
import sys

from tests.test import Case, test_me


class Stack:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def push(self, item):
        return self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


def solution(stack: Stack):
    """
    Keep popping elements until you find an element thats smaller than tmp

    then place tmp on its place

    """
    l_stack = stack
    r_stack = Stack()

    while not l_stack.is_empty():
        tmp = l_stack.pop()
        while not r_stack.is_empty() and r_stack.peek() > tmp:
            l_stack.push(r_stack.pop())
        r_stack.push(tmp)

    return r_stack.items


def solution2(stack: Stack):
    """
    Keep popping elements until you find an element thats smaller than tmp

    then place tmp on its place

    """
    l_stack = stack
    r_stack = Stack()

    num_elems = 0
    max_num = sys.maxsize
    while not l_stack.is_empty():
        tmp = l_stack.pop()
        r_stack.push(tmp)
        num_elems += 1
        if tmp < max_num:
            max_num = tmp

    l_stack.push(max_num)

    iter_count = 0
    while num_elems != 0:
        if iter_count % 2 == 0:
            for i in range(num_elems):
                tmp = r_stack.pop()
                if tmp == max_num:
                    continue
                l_stack.push(tmp)
            num_elems = num_elems - 1
        elif iter_count % 2 == 1:
            max_num = sys.maxsize
            for i in range(num_elems):
                tmp = l_stack.pop()
                if tmp < max_num:
                    max_num = tmp
                r_stack.push(tmp)
            l_stack.push(max_num)
        iter_count += 1
    return l_stack.items


element = Stack()
lst = list(range(5000))
lst = random.sample(lst, len(lst))
# lst = [3, 2, 1, 5]
for i in lst:
    element.push(i)


test_cases: list[Case] = [
    {
        "i": (element),
        "o": list(sorted(lst)),
    },
]

test_functions = [solution, solution2]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

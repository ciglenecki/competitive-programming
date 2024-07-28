from __future__ import annotations

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


class QueueViaStacks:
    def __init__(self) -> None:
        self.fresh_stack = Stack()
        self.reserve_stack = Stack()

    def push(self, item):
        self.fresh_stack.push(item)

    def move_fresh_to_reserve(self):
        if len(self.reserve_stack) == 0:
            while not self.fresh_stack.is_empty():
                self.reserve_stack.push(self.fresh_stack.pop())

    def pop(self):
        self.move_fresh_to_reserve()
        self.reserve_stack.pop()

    def peek(self):
        self.move_fresh_to_reserve()
        self.reserve_stack.peek()

    def get_state(self):
        return [self.fresh_stack.items, self.reserve_stack.items]


def solution(qvs: QueueViaStacks):
    return qvs.get_state()


qvs = QueueViaStacks()
qvs.push(1)
qvs.push(2)
qvs.push(3)
qvs.pop()
qvs.push(4)
qvs.push(5)

qvs2 = QueueViaStacks()
qvs2.push(1)
qvs2.pop()
qvs2.push(2)
qvs2.pop()

test_cases: list[Case] = [
    {
        "i": (qvs),
        "o": [[4, 5], [3, 2]],
    },
    {
        "i": (qvs2),
        "o": [[], []],
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

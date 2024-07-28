from __future__ import annotations

from tests.test import Case, test_me


class Stack:
    def __init__(self) -> None:
        self.items = []

    @staticmethod
    def from_list(items: list):
        stack = Stack()
        stack.items = items
        return stack

    def pop(self):
        self.items.pop(-1)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


def solution(ll: LL):
    node = ll.head
    if node is None:
        return None
    store = set()
    while node is not None:
        if node.value in store:
            return node.value
        store.add(node.value)
        node = node.next
    return None


test_cases: list[Case] = [
    {
        "i": (Stack.from_list([1, 2, 3, 4, 3]),),
        "o": 3,
    }
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

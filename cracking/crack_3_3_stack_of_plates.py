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


class SetOfStacks:
    def __init__(self, max_capacity: int) -> None:
        self.max_capacity = max_capacity
        self.stacks: list[Stack] = [Stack()]

    def push(self, item):
        last_stack = self.stacks[-1]
        if len(last_stack) != self.max_capacity:
            last_stack.push(item)
            return
        new_stack = Stack()
        new_stack.push(item)
        self.stacks.append(new_stack)
        return

    def pop(self):
        last_stack = self.stacks[-1]
        item = last_stack.pop()
        if len(last_stack) == 0:
            self.stacks.pop()
        return item

    def peek(self):
        last_stack = self.stacks[-1]
        return last_stack.peek()

    def get_state(self):
        result = []
        for stack in self.stacks:
            result.append(stack.items)
        return result


def solution(sos: SetOfStacks):
    return sos.get_state()


sos = SetOfStacks(max_capacity=3)
sos.push(1)
sos.push(2)
sos.push(3)
sos.push(4)
sos.push(5)
sos.push(6)
sos.push(7)

test_cases: list[Case] = [
    {
        "i": (sos),
        "o": [[1, 2, 3], [4, 5, 6], [7]],
    }
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

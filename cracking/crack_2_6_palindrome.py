from __future__ import annotations
from tests.test import Case, test_me

"""
Implement a function to check if a linked list is a palindrome.
"""

# reimplement node class
class Node:
    def __init__(self, value, next: Node | None = None, prev: Node | None = None):
        self.value = value
        self.next = next
        self.prev = prev

    def switch(self, node: Node):
        simple = True

        if simple:
            node.value, self.value = self.value, node.value
        else:
            tmp_prev = node.prev
            tmp_next = node.next

            node.next = self.next
            node.prev = self.prev

            self.next = tmp_prev
            self.prev = tmp_next
        return self

    def remove(self):
        if self.next is not None:
            self.next.prev = self.prev
        if self.prev is not None:
            self.prev.next = self.next
        self.prev = None
        self.next = None
        return self

    def insert_after(self, value):
        new_node = Node(value, self.next, self)
        if self.next is not None:
            self.next.prev = new_node
        self.next = new_node
        return self

    def insert_before(self, value):
        new_node = Node(value, self, self.prev)
        if self.prev is not None:
            self.prev.next = new_node
        self.prev = new_node
        return self

    def __eq__(self, other: Node):
        return self.value == other.value

    def __str__(self):
        return f"({self.value})"


class LL:
    def __init__(self, head: Node | None = None):
        self.head = head
        self.count = 0

    @staticmethod
    def create_from_list(elements: list):
        ll = LL()
        if len(elements) == 0:
            return ll
        ll.head = Node(elements[0])
        tmp_node = ll.head

        for e in elements[1:]:
            if tmp_node is not None:
                tmp_node.insert_after(e)
                if tmp_node.next:
                    tmp_node = tmp_node.next

        ll.count = len(elements)
        return ll

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value)
            return self

        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.insert_after(value)
        return self

    def insert_at_start(self, value):
        if self.head is None:
            self.head = Node(value)
            return self

        self.head.insert_before(value)
        self.head = self.head.prev
        return self

    def __str__(self) -> str:
        if not self.head:
            return "Empty"

        string = ""
        string += str(self.head.value)

        tmp_node = self.head
        while tmp_node.next is not None:
            tmp_node = tmp_node.next
            if hasattr(tmp_node, "prev") and tmp_node.prev is not None:
                string += "<=>"
            else:
                string += "=>"
            string += str(tmp_node.value)
        return string

    def __ne__(self, other: LL):
        return not self.__eq__(other)

    def __eq__(self, other: LL):

        head1 = self.head
        head2 = other.head

        while head1 is not None and head2 is not None:
            if head1 != head2:
                return False

            head1 = head1.next
            head2 = head2.next
        return True


def my_floor(num: float | int):
    num_ = int(num)
    if num_ >= 0 or num == num_:
        return num_
    return num_ - 1


def solution_copy_reversed(ll: LL):
    if ll.head is None:
        return False

    ll_reversed = LL()
    tail = ll.head
    length = 0

    while tail is not None:
        ll_reversed.insert_at_start(tail.value)
        tail = tail.next
        length += 1

    length = my_floor(length / 2)
    head_1 = ll.head
    head_2 = ll_reversed.head

    while length != 0:
        if head_1.value != head_2.value:
            return False
        head_1 = head_1.next
        head_2 = head_2.next
        length -= 1

    return True


def solution_runner(ll: LL):

    """
    Use the runner method to get to the 'middle' of the linked list. While moving the the middle, add elements to the stack. Once we come the middle (if the number is odd do some more work) we start going from the middle to the end. We last half elements from the stack, which holds the first half.
    """

    slow = ll.head

    if slow is None:
        return False

    if slow.next is None:  # one element -> True
        return True

    if slow.next.next is None:  # true elements -> True if same
        return slow.value == slow.next.value

    stack = []
    stack.append(slow.value)

    fast = ll.head.next

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        stack.append(slow.value)

    slow = slow.next
    if fast.next is not None:  # the number of elements is odd, so skip
        slow = slow.next

    while slow is not None:
        if slow.value != stack.pop():
            return False
        slow = slow.next

    return True


test_cases: list[Case] = [
    {
        "i": LL.create_from_list([]),
        "o": False,
    },
    {
        "i": LL.create_from_list(["a", "b", "c", "b", "a"]),
        "o": True,
    },
    {
        "i": LL.create_from_list(["a"]),
        "o": True,
    },
    {
        "i": LL.create_from_list(["a", "b", "a"]),
        "o": True,
    },
    {
        "i": LL.create_from_list(["a", "b", "b", "a"]),
        "o": True,
    },
    {
        "i": LL.create_from_list(["a", "b", "c", "a"]),
        "o": False,
    },
    {
        "i": LL.create_from_list(["a", "a"]),
        "o": True,
    },
    {
        "i": LL.create_from_list([0, 0, 0]),
        "o": True,
    },
    {
        "i": LL.create_from_list([1, 0, 1]),
        "o": True,
    },
    {
        "i": LL.create_from_list([1, 0, 0, 1]),
        "o": True,
    },
]

test_functions = [solution_copy_reversed, solution_runner]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

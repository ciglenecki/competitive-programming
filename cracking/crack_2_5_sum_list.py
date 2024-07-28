from __future__ import annotations
from tests.test import Case, test_me

"""
Sum Lists:

You have two numbers represented by a linked list, where each node contains a single digit.

The digits are stored in reverse order, such that the 1 's digit is at the head of the list.

Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input:(7 -> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP

Suppose the digits are stored in forward order. Repeat the above problem.

EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
Hints: #7, #30, #71, #95, #109

"""

# reimplement node class
class Node:
    def __init__(self, value, next: Node | None = None, prev: Node | None = None):
        self.value = value
        self.next = None
        self.prev = None

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
        self.prev_node = None
        self.next_node = None
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
            if hasattr(tmp_node, "prev_node") and tmp_node.prev_node is not None:
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


def solution(ll1: LL, ll2: LL):
    ll_result = LL()
    if ll1.head is None or ll2.head is None:
        raise Exception(f"Invalid lists {ll1, ll2}")
    tmp_node_1 = ll1.head
    tmp_node_2 = ll2.head
    carry = 0
    while (tmp_node_1 is not None and tmp_node_2 is not None) or carry:
        if tmp_node_1 is None and tmp_node_2 is None:
            ll_result.insert_at_end(carry)
            return ll_result

        v1 = tmp_node_1.value if tmp_node_1 else 0
        v2 = tmp_node_2.value if tmp_node_2 else 0

        sum_ = v1 + v2 + carry
        carry = bool(sum_ >= 10)
        value = sum_ % 10
        ll_result.insert_at_end(value)

        tmp_node_1 = tmp_node_1.next if tmp_node_1 else None
        tmp_node_2 = tmp_node_2.next if tmp_node_2 else None

    return ll_result


test_cases: list[Case] = [
    {
        "i": (LL.create_from_list([7, 1, 6]), LL.create_from_list([5, 9, 2])),
        "o": LL.create_from_list([2, 1, 9]),
    },
    {
        "i": (LL.create_from_list([9, 9, 9]), LL.create_from_list([9, 9, 9])),
        "o": LL.create_from_list([8, 9, 9, 1]),
    },
    {
        "i": (LL.create_from_list([9, 9, 9]), LL.create_from_list([1])),
        "o": LL.create_from_list([0, 0, 0, 1]),
    },
    {
        "i": (LL.create_from_list([1]), LL.create_from_list([1])),
        "o": LL.create_from_list([2]),
    },
    {
        "i": (LL.create_from_list([0, 1]), LL.create_from_list([0])),
        "o": LL.create_from_list([0, 1]),
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

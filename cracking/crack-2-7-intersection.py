from __future__ import annotations
from tests.test import Case, test_me

"""
Note: solution will be created for intersacting value, not reference (assumption, elements are unique in each linked list)

Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

Idea: pass through the first list. Add everything to set. Pass through the second list and check if any of them are in the set.

Idea 2:
1 - 2 - 5 - 6 - 7 - 4 - 3
            5 - 7 - 4 - 3

Caculate length of each LL O(n) * 2

Caculate the difference between lenghts and use that number to skip the first n parts in the longer list

6 - 7 - 4 - 3
5 - 7 - 4 - 3

now start comparing each element.
If elements are same and saved intersection is None => set saved intersection
if elements are different => clear saved intersction
If elements are same and saved intersection is NOT None => do nothing 
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


def solution(la, lb):

    head_a = la.head
    head_b = lb.head
    if head_a is None or head_b is None:
        return -1

    len_a = 1
    while head_a.next is not None:
        head_a = head_a.next
        len_a += 1

    len_b = 1
    while head_b.next is not None:
        head_b = head_b.next
        len_b += 1

    if head_a.value != head_b.value:
        # if last element is not the same there's no intersection
        return -1

    if len_a > len_b:
        bigger = la.head
        smaller = lb.head
        diff = len_a - len_b
    else:
        bigger = lb.head
        smaller = la.head
        diff = len_b - len_a

    while diff != 0:
        bigger = bigger.next
        diff -= 1

    intersection = None

    while bigger is not None or smaller is not None:

        if bigger.value == smaller.value and intersection is None:
            intersection = bigger.value
        elif bigger.value != smaller.value:
            intersection = None

        bigger = bigger.next
        smaller = smaller.next

    return intersection


test_cases: list[Case] = [
    {
        "i": (
            LL.create_from_list([1, 2, 5, 6, 7, 4, 3]),
            LL.create_from_list([5, 7, 4, 3]),
        ),
        "o": 7,
    },
    {
        "i": (
            LL.create_from_list([1, 2, 5, 6, 7, 4, 3]),
            LL.create_from_list([6, 0, 4, 3]),
        ),
        "o": 4,
    },
    {
        "i": (
            LL.create_from_list([1]),
            LL.create_from_list([1]),
        ),
        "o": 1,
    },
    {
        "i": (
            LL.create_from_list([]),
            LL.create_from_list([1]),
        ),
        "o": -1,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

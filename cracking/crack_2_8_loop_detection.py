from __future__ import annotations

from tests.test import Case, test_me

"""

Note: 
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.

Input:
A -> B -> C -> D -> E -> C [the same C as earlier]
Output:
C
 

"""


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

    def __repr__(self) -> str:
        return self.__str__()

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
        "i": (LL.create_from_list([1, 2, 3, 4, 3]),),
        "o": 3,
    },
    {
        "i": (LL.create_from_list([1, 2, 3, 4, 5]),),
        "o": None,
    },
    {
        "i": (LL.create_from_list([1]),),
        "o": None,
    },
    {
        "i": (LL.create_from_list([1, 2]),),
        "o": None,
    },
    {
        "i": (LL.create_from_list([]),),
        "o": None,
    },
    {
        "i": (LL.create_from_list([1, 2, 3, 3]),),
        "o": 3,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

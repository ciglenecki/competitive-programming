import sys

sys.path.append("..")
from test import Case, test_me
from structs import linked_list

"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""


def remove_dups_seen(ll: linked_list.DoubleLinkedList):
    """
    O(n)
    """

    tmp_node = ll.head
    if not tmp_node:
        return []

    seen = {}
    result = []

    while tmp_node is not None:
        if tmp_node.data in seen:
            if tmp_node.next_node:
                tmp_node.next_node.prev_node = tmp_node.prev_node
            if tmp_node.prev_node:
                tmp_node.prev_node.next_node = tmp_node.next_node
        else:
            seen[tmp_node.data] = True
            result.append(tmp_node.data)
        tmp_node = tmp_node.next_node
    return result


def remove_dups_no_buff(ll: linked_list.DoubleLinkedList):
    """
    O(n) + O(n-1) + O(n - 2) ... + O(1)

    O(n * (n-1) / 2)

    O(n^2)
    """

    node = ll.head

    if not node:
        return []

    result = []

    while node is not None:
        tmp_node = node.next_node

        while tmp_node is not None:
            if tmp_node.data == node.data:
                if tmp_node.next_node:
                    tmp_node.next_node.prev_node = tmp_node.prev_node
                if tmp_node.prev_node:
                    tmp_node.prev_node.next_node = tmp_node.next_node
            tmp_node = tmp_node.next_node

        result.append(node.data)
        node = node.next_node

    return result


test_cases: list[Case] = [
    {
        "i": linked_list.DoubleLinkedList().create_from_list(
            [1, 2, 3, 3, 4, 5, 6, 6, 7, 7]
        ),
        "o": [1, 2, 3, 4, 5, 6, 7],
    },
    {
        "i": linked_list.DoubleLinkedList().create_from_list(
            [1, 2, 1, 1, 2, 2, 2, 1, 2]
        ),
        "o": [1, 2],
    },
    {
        "i": linked_list.DoubleLinkedList(),
        "o": [],
    },
    {
        "i": linked_list.DoubleLinkedList().insert_at_end(1),
        "o": [1],
    },
    {
        "i": linked_list.DoubleLinkedList().create_from_list([1, 2]),
        "o": [1, 2],
    },
    {
        "i": linked_list.DoubleLinkedList().create_from_list([1, 1]),
        "o": [1],
    },
]

test_functions = [remove_dups_seen, remove_dups_no_buff]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

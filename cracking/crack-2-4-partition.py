from test import Case, test_me
from structs import linked_list

"""
note: this question is weirdly phrased. My implementation finds the Node with value `value` and delets it from the linked list.


Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

EXAMPLE

lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks likea->b->d->e- >f


Idea 1: insert all elements < to the start O(n)

Idea 2: create 2 linked lists and merge them together
"""


def pratition(ll: linked_list.DoubleLinkedList, value: int):
    head = ll.head
    if head is None:
        return ll

    curr_node = head
    while curr_node is not None:
        if curr_node.data < value and curr_node is not head:
            # save the gap
            tmp_node = curr_node.next_node

            # stitch the gap
            if curr_node.prev_node is not None:
                curr_node.prev_node.next_node = curr_node.next_node

            if curr_node.next_node is not None:
                curr_node.next_node.prev_node = curr_node.prev_node

            # insert the new head
            curr_node.next_node = head
            head.prev_node = curr_node
            head = curr_node
            ll.head = head

            curr_node = tmp_node
        else:
            curr_node = curr_node.next_node

    return ll


test_cases: list[Case] = [
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([1, 2, 3, 4, 5]), 3),
        "o": linked_list.DoubleLinkedList().create_from_list([2, 1, 3, 4, 5]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([5, 3, 1, 4, 5, 2]), 4),
        "o": linked_list.DoubleLinkedList().create_from_list([2, 1, 3, 5, 4, 5]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([]), 4),
        "o": linked_list.DoubleLinkedList().create_from_list([]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([4, 2]), 4),
        "o": linked_list.DoubleLinkedList().create_from_list([2, 4]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([4]), 4),
        "o": linked_list.DoubleLinkedList().create_from_list([4]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([3]), 4),
        "o": linked_list.DoubleLinkedList().create_from_list([3]),
    },
    {
        "i": (
            linked_list.DoubleLinkedList().create_from_list([3, 5, 8, 5, 10, 2, 1]),
            5,
        ),
        "o": linked_list.DoubleLinkedList().create_from_list([1, 2, 3, 5, 8, 5, 10]),
    },
]

test_functions = [pratition]

if __name__ == "__main__":
    # one = linked_list.DoubleLinkedList().create_from_list([1, 2, 3, 4, 5])
    # delete_middle(one.head.next_node.next_node)
    # print(one)
    # if one != linked_list.DoubleLinkedList().create_from_list([1, 2, 4, 5]):
    #     print("error one")
    test_me(test_cases, test_functions)

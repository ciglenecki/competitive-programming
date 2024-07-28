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

"""


def delete_middle(ll: linked_list.DoubleLinkedList, value: int):

    if ll.head is None:
        return ll

    curr_node = ll.head

    """
    we have to itterate from the perspective of the parent (parent node of the child with value `value`) because we need to reference the parent to connect the child's next node to the parent.
    """
    while curr_node.next_node is not None and curr_node.next_node.next_node is not None:
        if curr_node.next_node.data == value:
            curr_node.next_node = curr_node.next_node.next_node
            curr_node.next_node.prev_node = curr_node
            return ll
        curr_node = curr_node.next_node

    return ll


def delete_middle_c(ll: linked_list.DoubleLinkedList, value: int):

    if ll.head is None:
        return ll

    curr_node = ll.head

    while curr_node.next_node is not None and curr_node.next_node.next_node is not None:
        if curr_node.next_node.data == value:
            tmp_node = curr_node.next_node.next_node
            curr_node.next_node.next_node = None  # free()
            curr_node.next_node = tmp_node
            curr_node.next_node.prev_node = curr_node
            return ll
        curr_node = curr_node.next_node

    return ll


test_cases: list[Case] = [
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([]), 3),
        "o": linked_list.DoubleLinkedList().create_from_list([]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([3]), 3),
        "o": linked_list.DoubleLinkedList().create_from_list([]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([3, 4]), 3),
        "o": linked_list.DoubleLinkedList().create_from_list([3, 4]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([3, 4, 3]), 3),
        "o": linked_list.DoubleLinkedList().create_from_list([3, 4, 3]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([3, 4, 3]), 4),
        "o": linked_list.DoubleLinkedList().create_from_list([3, 3]),
    },
    {
        "i": (linked_list.DoubleLinkedList().create_from_list([3, 4, 4, 3]), 4),
        "o": linked_list.DoubleLinkedList().create_from_list([3, 4, 3]),
    },
]

test_functions = [delete_middle, delete_middle_c]

if __name__ == "__main__":
    # one = linked_list.DoubleLinkedList().create_from_list([1, 2, 3, 4, 5])
    # delete_middle(one.head.next_node.next_node)
    # print(one)
    # if one != linked_list.DoubleLinkedList().create_from_list([1, 2, 4, 5]):
    #     print("error one")
    test_me(test_cases, test_functions)

from test import Case, test_me

from structs import linked_list

"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""


def solution(ll: linked_list.DoubleLinkedList, k: int):
    node = ll.head
    if not node:
        return 0

    def finder(node, count):
        """
        Go the the end of the list and hold the count.
        Keep returning the count - k in recusion until one node has that count value
        """

        if node is None:
            return count - k

        result = finder(node.next_node, count + 1)

        if result == count + 1:
            return node.data
        else:
            return result

    return finder(node, 0)


test_cases: list[Case] = [
    {
        "i": (
            linked_list.DoubleLinkedList().create_from_list(
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ),
            5,
        ),
        "o": 4,
    },
    {
        "i": (
            linked_list.DoubleLinkedList().create_from_list(
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ),
            0,
        ),
        "o": 9,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

from __future__ import annotations

from enum import Enum
from typing import Optional

from structs import linked_list
from tests.test import Case, test_me


class State(Enum):
    VISITED = "visited"
    NOT_VISITED = "not_visited"


class BinaryNode:
    def __init__(
        self,
        item,
        left: Optional[BinaryNode] = None,
        right: Optional[BinaryNode] = None,
    ):
        self.item = item
        self.left = left
        self.right = right

    def __eq__(self, other: BinaryNode):
        return other.item == self.item

    def get_state(self):
        right_state = None if self.right is None else self.right.get_state()
        left_state = None if self.left is None else self.left.get_state()
        return [self.item, [left_state, right_state]]

    def __repr__(self) -> str:
        return str(self.item)


def solution(tree: BinaryNode) -> list[linked_list.DoubleLinkedList]:
    """
    LinkedList:
        (Node (BinaryNode)) ->
        (Node (BinaryNode)) ->
        ...
    """
    result = list[linked_list.DoubleLinkedList]()

    ll = linked_list.DoubleLinkedList(
        head=linked_list.Node[BinaryNode](tree),
    )

    parents = ll
    while len(parents) != 0:
        result.append(parents)
        new_ll = linked_list.DoubleLinkedList()

        for node_ll in parents:
            node: BinaryNode = node_ll.data
            right, left = node.right, node.left
            if left is not None:
                new_ll.insert_at_end(left)
            if right is not None:
                new_ll.insert_at_end(right)
        parents = new_ll

    ints_only = []
    for ll in result:
        ints_only.append([node_ll.data.item for node_ll in ll])
    return ints_only


test_cases: list[Case] = [
    {
        "i": BinaryNode(
            5,
            left=BinaryNode(
                1,
                left=BinaryNode(
                    3,
                    left=BinaryNode(4),
                ),
                right=BinaryNode(2),
            ),
            right=BinaryNode(6),
        ),
        "o": [[5], [1, 6], [3, 2], [4]],
    },
    {
        "i": BinaryNode(5),
        "o": [[5]],
    },
    {
        "i": BinaryNode(5, right=BinaryNode(6, right=BinaryNode(7))),
        "o": [[5], [6], [7]],
    },
    {
        "i": BinaryNode(
            5,
            right=BinaryNode(6, left=BinaryNode(8), right=BinaryNode(7)),
        ),
        "o": [[5], [6], [8, 7]],
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

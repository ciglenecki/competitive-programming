from __future__ import annotations

import sys
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
        string = str((self.item, self.left, self.right))
        return string


def solution(tree: BinaryNode) -> bool:
    """
    LinkedList:
        (Node (BinaryNode)) ->
        (Node (BinaryNode)) ->
        ...
    """

    def is_bst(node: Optional[BinaryNode], max_: Optional[int], min_: Optional[int]):
        if node is None:
            return True
        if max_ is not None and node.item > max_:
            return False
        if min_ is not None and node.item < min_:
            return False

        is_bst_left = is_bst(node.left, max_=node.item, min_=min_)
        is_bst_right = is_bst(node.right, max_=max_, min_=node.item)
        return is_bst_left and is_bst_right

    return is_bst(tree, None, None)


test_cases: list[Case] = [
    {
        "i": BinaryNode(
            5,
        ),
        "o": True,
    },
    {
        "i": BinaryNode(
            5,
            left=BinaryNode(
                2,
                left=BinaryNode(1),
            ),
            right=BinaryNode(8),
        ),
        "o": True,
    },
    {
        "i": BinaryNode(
            5,
            left=BinaryNode(2, left=BinaryNode(1), right=BinaryNode(3)),
            right=BinaryNode(8, left=BinaryNode(7), right=BinaryNode(9)),
        ),
        "o": True,
    },
    {
        "i": BinaryNode(
            8,
            left=BinaryNode(2, left=BinaryNode(1), right=BinaryNode(3)),
            right=BinaryNode(8, left=BinaryNode(7), right=BinaryNode(9)),
        ),
        "o": False,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

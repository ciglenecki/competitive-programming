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
        string = str((self.item, self.left, self.right))
        return string


def solution(tree: BinaryNode):
    """
    LinkedList:
        (Node (BinaryNode)) ->
        (Node (BinaryNode)) ->
        ...
    """

    def get_depth(node: Optional[BinaryNode], depth: int) -> int:
        if node is None:
            return depth - 1
        left_depth = get_depth(node.left, depth + 1)
        right_depth = get_depth(node.right, depth + 1)
        return max(left_depth, right_depth)

    def is_balanced(node: Optional[BinaryNode], depth=0):
        if node is None:
            return True

        left_depth = get_depth(node.left, depth + 1)
        right_depth = get_depth(node.right, depth + 1)

        diff = left_depth - right_depth
        if diff >= 2 or diff <= -2:
            return False

        is_left_balanced = is_balanced(node.left)
        is_right_balanced = is_balanced(node.right)
        return is_left_balanced and is_right_balanced

    return is_balanced(tree)


test_cases: list[Case] = [
    {
        "i": BinaryNode(
            5,
            right=BinaryNode(
                1,
                right=BinaryNode(2),
            ),
            left=BinaryNode(3),
        ),
        "o": True,
    },
    {
        "i": BinaryNode(
            5,
            right=BinaryNode(
                1,
                right=BinaryNode(2),
            ),
        ),
        "o": False,
    },
    {
        "i": BinaryNode(
            5,
            left=BinaryNode(
                1,
                left=BinaryNode(
                    3,
                ),
                right=BinaryNode(2),
            ),
            right=BinaryNode(6),
        ),
        "o": True,
    },
    {
        "i": BinaryNode(
            5,
            left=BinaryNode(
                1,
                left=BinaryNode(3, right=BinaryNode(4)),
                right=BinaryNode(2),
            ),
            right=BinaryNode(6),
        ),
        "o": False,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

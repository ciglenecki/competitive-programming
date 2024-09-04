"""
For a given node of a binary search tree, find it's successor.

layman terms: given an original node, find a node whose value is the smallest but still bigger than original node.

Assumption: node has a link to it's parent.
Assumption: the logic of comparing node's values is hidden from you (you shouldn't compare node_a.value > node_b.value)

We can find a successor without comparing node values because the nature of binary search tree stores elements in a particual way. The left subtree of a node contains only smaller nodes, while the right subtree of a node contains only larger nodes.

Solution:

(case A)
if the node has a right subtree, then surely the successor node will be in that subtree. The successor can't be above a node, because we know those values will be larger than values in the right subtree.
Now that we are in the right subtree, we know that all nodes are potential successors since their values are larger than original node's. To find a successor, we have to find the smallest node within the right subtree. This is simply the left-most (bottom left) node in the right subtree.

(case B)
if original node doesn't have a right subtree then it's a leaf.
The successor is somewhere above the original node. We have to climb up to find a node whose value is larger than original node's. However, we have to be careful when climbing up.
    - if the parent is on the left side of the child, the parent is smaller than it's child
    - if the parent is on the right side of the child, the parent is larger than it's child
If the parent is smaller, we have to continue with traversing up until we reach a parent who is larger than the original node. If we reach such a parent, he is the successor.
    - Why? because the right subtree of that parent only contains nodes which are larger (too large! we are finding the smallest possible value which is larger than original node)

(case B2)
If we can't find a parent who comes from a right side, then the original node is the right-most (bottom right) node, and it has no successor -> None is returned
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

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
        self.parent: BinaryNode | None = None
        self.left = left
        self.right = right
        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self

    def __eq__(self, other: BinaryNode):
        return other.item == self.item

    def get_state(self):
        right_state = None if self.right is None else self.right.get_state()
        left_state = None if self.left is None else self.left.get_state()
        return [self.item, [left_state, right_state]]

    def __repr__(self) -> str:
        string = str((self.item, self.left, self.right))
        return string


def solution(tree: BinaryNode) -> int | None:
    """
    LinkedList:
        (Node (BinaryNode)) ->
        (Node (BinaryNode)) ->
        ...
    """

    def left_most_child(node: BinaryNode):
        assert node.right is not None
        node = node.right
        while node.left is not None:
            node = node.left
        return node

    def find_successor(node: BinaryNode):
        has_right = node.right is not None
        if has_right:
            return left_most_child(node)

        curr = node
        parent = node.parent
        while parent is not None and curr != parent.left:
            curr = parent
            parent = parent.parent
        return parent

    successor = find_successor(tree)
    if successor:
        return successor.item
    return successor


tree = BinaryNode(
    20,
    left=BinaryNode(
        8,
        left=BinaryNode(4),
        right=BinaryNode(
            12,
            left=BinaryNode(10),
            right=BinaryNode(14),
        ),
    ),
    right=BinaryNode(22),
)

test_cases: list[Case] = [
    {
        "i": tree.left,  # 8,
        "o": 10,
    },
    {
        "i": tree.left.right.left,  # 10
        "o": 12,
    },
    {
        "i": tree.left.right.right,  # 10
        "o": 20,
    },
    {
        "i": tree.right,  # 10
        "o": None,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

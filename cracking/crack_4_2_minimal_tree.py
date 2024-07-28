from __future__ import annotations

from enum import Enum
from queue import Queue
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
        self.left = left
        self.right = right

    def __eq__(self, other: BinaryNode):
        return other.item == self.item

    def get_state(self):
        right_state = None if self.right is None else self.right.get_state()
        left_state = None if self.left is None else self.left.get_state()
        return [self.item, [left_state, right_state]]


def inner(num_list: list[int]):
    if len(num_list) == 1:
        return BinaryNode(item=num_list[0])

    mid_index = len(num_list) // 2
    mid_item = num_list[mid_index]
    node_left = inner(num_list[:mid_index])
    if len(num_list) > 2:
        node_right = inner(num_list[mid_index + 1 :])
    else:
        node_right = None
    node = BinaryNode(item=mid_item, right=node_right, left=node_left)
    return node


def solution(num_list: list[int]) -> list:
    return inner(num_list).get_state()


num_list_1 = sorted([1, 2, 3])
num_list_2 = sorted([1, 2, 3, 4, 5, 6])
num_list_3 = sorted([1, 2, 3, 4, 5, 6, 7])

test_cases: list[Case] = [
    {
        "i": (num_list_1),
        "o": [2, [[1, [None, None]], [3, [None, None]]]],
    },
    {
        "i": (num_list_2),
        "o": [
            4,
            [
                [
                    2,
                    [
                        [1, [None, None]],
                        [3, [None, None]],
                    ],
                ],
                [
                    6,
                    [
                        [5, [None, None]],
                        None,
                    ],
                ],
            ],
        ],
    },
    {
        "i": (num_list_3),
        "o": [
            4,
            [
                [
                    2,
                    [
                        [1, [None, None]],
                        [3, [None, None]],
                    ],
                ],
                [
                    6,
                    [
                        [5, [None, None]],
                        [7, [None, None]],
                    ],
                ],
            ],
        ],
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

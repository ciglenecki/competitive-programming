"""
BST Sequences:


BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each element. 

Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

EXAMPLE
Input:
    2
/       \
1       3

Output: {2, 1, 3}, {2, 3, 1}

"""

from tests.test import Case, test_me


class Node:
    def __init__(self, name: int) -> None:
        self.name = name
        self.right: Node | None = None
        self.left: Node | None = None
        self.parent: Node | None = None

    def add_parent(self, node: "Node"):
        self.parent = node

    def __repr__(self) -> str:
        return str(self.name)


def combine(
    list_1: list[Node], list_2: list[Node], prefix: list[Node]
) -> list[list[Node]]:
    results = list[list[Node]]()

    if len(list_1) == 0 or len(list_2) == 0:
        # if one list is empty, that means that we cannot permute it no longer
        # also, the other list probably has only one element
        # which we add to the result
        result = prefix
        result.extend(list_1)
        result.extend(list_2)
        results.append(result)
        return results

    # we pick one element from the list, and add to the prefix
    # the rest of the elements get permuted recursively.
    first_result = combine(list_1[1:], list_2, [*prefix, *list_1[:1]])
    second_result = combine(list_2[1:], list_1, [*prefix, *list_2[:1]])

    results.extend(first_result)
    results.extend(second_result)
    return results


def combine2(
    list_1: list[Node], list_2: list[Node], prefix: list[Node]
) -> list[list[Node]]:
    results = list[list[Node]]()

    if len(list_1) == 0 or len(list_2) == 0:
        result = prefix
        result.extend(list_1)
        result.extend(list_2)
        print("result prefix", result)
        results.append(result)
        return results

    first_result = combine(list_1[1:], list_2, [*prefix, *list_1[:1]])
    second_result = combine(list_2[1:], list_1, [*prefix, *list_2[:1]])

    results.extend(first_result)
    results.extend(second_result)
    return results


def solution(n: Node | None) -> list[list[Node]]:
    if n is None:
        # we reached a leaf, the leaf should return empty sequence
        # but it should contain one element because we have to perform a for loop (n=1) for that starting right/left element
        return [[]]

    prefix = [n]
    results = list[list[Node]]()
    left_seqs = solution(n.left)
    right_seqs = solution(n.right)

    for left_seq in left_seqs:
        for right_seq in right_seqs:
            result = combine(list_1=left_seq, list_2=right_seq, prefix=prefix)

            results.extend(result)

    return results


root = Node(name=30)
left_0 = Node(name=20)
root.left = left_0
right_0 = Node(60)
root.right = right_0
left_1_0 = Node(10)


left_0.left = left_1_0
left_0_1 = Node(25)
left_0.right = left_0_1

right_1_0 = Node(70)
right_0.right = right_1_0

right_2_0 = Node(65)
right_1_0.left = right_2_0
right_2_1 = Node(80)
right_1_0.right = right_2_0

left_1_1 = Node(25)
right_0.right = left_1_1
right_0.left = left_1_0

left_2_0 = Node(5)
left_1_0.left = left_2_0
left_2_1 = Node(15)
left_1_0.right = left_2_1


test_cases: list[Case] = [
    {
        "i": (left_0),
        "o": None,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
"""

from tests.test import Case, test_me


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.parent: Node | None = None

    def add_parent(self, node: "Node"):
        self.parent = node

    def __repr__(self) -> str:
        return self.name


def get_depth(n: Node) -> int:
    depth = 0
    curr = n

    while curr is not None:
        depth += 1
        curr = curr.parent

    return depth


def solution(a: Node, b: Node) -> str | None:
    diff = get_depth(a) - get_depth(b)  # 2 - 4

    # determinate which node is deeper
    if diff < 0:
        deeper = b
        shallower = a
    else:
        deeper = a
        shallower = b

    diff = -diff if diff < 0 else diff
    curr_a = deeper
    curr_b = shallower

    # bring up the deeper node to the same level as shallower node
    for _ in range(diff):
        curr_a = deeper.parent
    if curr_a == curr_b:
        return curr_a.name

    # compare nodes on the same level until we end up with a common ancestors
    while curr_a is not None and curr_b is not None and curr_a != curr_b:
        curr_a = curr_a.parent
        curr_b = curr_b.parent
    curr_a = None if curr_a is None or curr_b is None else curr_a.name
    return curr_a


a = Node(name="a")
b = Node(name="b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
i = Node("i")

h.add_parent(e)
i.add_parent(e)
d.add_parent(b)
e.add_parent(b)
f.add_parent(c)
g.add_parent(c)
b.add_parent(a)
c.add_parent(a)


test_cases: list[Case] = [
    {
        "i": (h, d),
        "o": b.name,
    },
    {
        "i": (b, c),
        "o": a.name,
    },
    {
        "i": (a, a),
        "o": a.name,
    },
    {
        "i": (f, h),
        "o": a.name,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

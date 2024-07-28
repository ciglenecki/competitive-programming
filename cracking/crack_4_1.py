from __future__ import annotations

from enum import Enum
from queue import Queue
from typing import Optional

from tests.test import Case, test_me


class State(Enum):
    VISITED = "visited"
    NOT_VISITED = "not_visited"


class Node:
    def __init__(self, item, children: Optional[list[Node]] = None):
        self.item = item
        if children is None:
            children = list[Node]()
        self.children = children
        self.state = State.NOT_VISITED

    def add_child(self, node: Node):
        self.children.append(node)

    def __eq__(self, other: Node):
        assert isinstance(other, Node)
        return other.item == self.item


class Graph:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children

    def add_child(self, node: Node):
        self.children.append(node)


def solution(g: Graph, s: Node, e: Node):
    if s == e:
        return True

    q = Queue[Node]()
    for c in g.children:
        q.put(c)

    while not q.empty():
        node = q.get()
        node.state = State.VISITED
        for c in node.children:
            if c.state == State.VISITED:
                continue
            if c == e:
                return True
            c.state = State.VISITED
            q.put(c)
    return False


node_a = Node("a")
node_b = Node("b")
node_c = Node("c")
node_d = Node("d")
node_a.add_child(node_b)
node_a.add_child(node_c)
node_d.add_child(node_c)
graph1 = Graph(children=[node_a, node_b, node_c, node_d])

node_a = Node("a")
node_b = Node("b")
node_c = Node("c")
node_a.add_child(node_b)
node_b.add_child(node_c)
graph2 = Graph(children=[node_a, node_b, node_c])

node_a = Node("a")
node_b = Node("b")
node_c = Node("c")
node_a.add_child(node_b)
node_b.add_child(node_c)
graph2 = Graph(children=[node_a, node_b, node_c])


node_a = Node("a")
node_b = Node("b")
node_c = Node("c")
node_a.add_child(node_b)
node_c.add_child(node_b)
graph3 = Graph(children=[node_a, node_b, node_c])


test_cases: list[Case] = [
    {
        "i": (graph1, node_a, node_d),
        "o": False,
    },
    {
        "i": (graph2, node_a, node_c),
        "o": True,
    },
    {
        "i": (graph3, node_a, node_c),
        "o": False,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

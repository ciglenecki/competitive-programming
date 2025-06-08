from tests.test import Case, test_me


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = list["Node"]()
        self.map = dict[str, "Node"]()
        self.num_dependencies = 0

    def add_child(self, node: "Node"):
        self.children.append(node)
        self.map[node.name] = node
        node.num_dependencies += 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Graph:
    def __init__(self):
        self.nodes = list[Node]()
        self.map = dict[str, "Node"]()

    def get_or_create_node(self, name: str) -> Node:
        if name not in self.map:
            node = Node(name=name)
            self.nodes.append(node)
            self.map[name] = node
        return self.map[name]

    def add_edge(self, node_name_start: str, node_name_end: str):
        node_start = self.map[node_name_start]
        node_end = self.map[node_name_end]
        node_start.add_child(node_end)


def solution(node_names: list[str], dependencies: list[tuple[str, str]]):
    # build graph
    graph = Graph()
    for n in node_names:
        graph.get_or_create_node(n)
    for d in dependencies:
        node_name_start, node_name_end = d
        graph.add_edge(
            node_name_start=node_name_start,
            node_name_end=node_name_end,
        )

    order: list[Node | None] = [None] * len(node_names)
    nodes = [graph.get_or_create_node(node_name) for node_name in node_names]
    for n in nodes:
        n.children = n.children
    print("nodes", nodes)
    end_index = add_non_dependant_to_list(order=order, nodes=nodes, offset=0)
    counter = 0
    while counter < len(node_names):
        print("order", order)
        current_node = order[counter]

        if current_node is None:
            return None
        for n in current_node.children:
            print("removing dep", n.name)
            n.num_dependencies -= 1  # remove current_node dependecy
        end_index = add_non_dependant_to_list(
            order=order,
            nodes=current_node.children,
            offset=end_index,
        )
        counter += 1
        print()
    order_names = [n.name for n in order]
    return order_names


def add_non_dependant_to_list(order: list[Node], nodes: list[Node], offset: int):
    print("offset", offset)
    for node in nodes:
        print("node", node.name, node.num_dependencies)
        if node.num_dependencies == 0:
            print("adding", node.name)
            order[offset] = node
            offset += 1
    return offset


# tree = BinaryNode(
#     20,
#     left=BinaryNode(
#         8,
#         left=BinaryNode(4),
#         right=BinaryNode(
#             12,
#             left=BinaryNode(10),
#             right=BinaryNode(14),
#         ),
#     ),
#     right=BinaryNode(22),
# )

test_cases: list[Case] = [
    {
        "i": (
            ["a", "b", "c", "d", "e", "f"],
            [
                ("a", "d"),
                ("f", "a"),
                ("f", "b"),
                ("b", "d"),
                ("d", "c"),
            ],
        ),
        "o": ["e", "f", "a", "b", "d", "c"],
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

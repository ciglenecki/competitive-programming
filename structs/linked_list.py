from __future__ import annotations


class Node:
    def __init__(
        self, data, next_node: Node | None = None, prev_node: Node | None = None
    ) -> None:
        self.next_node = next_node
        self.prev_node = prev_node
        self.data = data

    def insert_after(self, data):
        """
        [x]<=>[5]
        [x]<=>[new]<=>[5]
        """
        new_node = Node(data, next_node=self.next_node, prev_node=self)
        if self.next_node is not None:
            self.next_node.prev_node = new_node
        self.next_node = new_node

    def insert_before(self, data):
        """
        [5]<=>[x]
        [5]<=>[new]<=>[x]
        """
        new_node = Node(data, next_node=self, prev_node=self.prev_node)
        if self.prev_node is not None:
            self.prev_node.next_node = new_node
        self.prev_node = new_node

    def remove(self):
        """
        [5]<=>[x]<=>[6]
        [5]<=>[6]
        """
        if self.next_node:
            self.next_node.prev_node = self.prev_node
        if self.prev_node:
            self.prev_node.next_node = self.next_node

        self.prev_node = None
        self.next_node = None

    def switch(self, node: Node):
        """
        [5]<=>...<=>[6]
        [6]<=>...<=>[5]
        """
        self.data, node.data = node.data, self.data

    def __str__(self) -> str:
        return str(self.data)


class DoubleLinkedList:
    def __init__(self, head: Node | None = None):
        self.head = head
        self.count = 0

    def create_from_list(self, elements: list):
        if len(elements) == 0:
            return None
        self.head = Node(elements[0])
        tmp_node = self.head

        for e in elements[1:]:
            tmp_node.insert_after(e)
            tmp_node = tmp_node.next_node

        self.count = len(elements)
        return self

    def insert_at_end(self, data) -> DoubleLinkedList:
        if self.head is None:
            self.head = Node(data)
            return self

        tmp_node = self.head
        while tmp_node.next_node is not None:
            tmp_node = tmp_node.next_node
        tmp_node.insert_after(data)
        self.count +=1
        return self

    def insert_at_start(self, data) -> DoubleLinkedList:
        if self.head is None:
            self.head = Node(data)
            self.count +=1
            return self

        self.head.insert_before(data)
        self.head = self.head.prev_node
        self.count +=1

        return self

    def find(self, data) -> Node | None:
        if self.head is None:
            return None

        tmp_node = self.head

        while tmp_node is not None:
            if tmp_node.data == data:
                return tmp_node
            tmp_node = tmp_node.next_node

        return None

    def remove(self, data) -> DoubleLinkedList:
        if self.head is None:
            return self

        tmp_node = self.find(data)

        if tmp_node:
            if tmp_node is self.head:
                self.head = tmp_node.next_node
            tmp_node.remove()
            self.count -= 1

        return self

    def runner_technique(self) -> DoubleLinkedList:
        if self.count % 2 != 0:
            raise Exception("Works only with even count")
        
        slow = self.head
        fast = self.head.next_node

        while fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node

        fast = self.head
        slow = slow.next_node

        while slow is not None:
            fast.next_node.switch(slow)
            slow = slow.next_node
            fast = fast.next_node.next_node

    def __len__(self):
        return self.count

    def __str__(self) -> str:
        if not self.head:
            return "Empty"

        string = ""
        string += str(self.head.data)

        tmp_node = self.head
        while tmp_node.next_node is not None:
            tmp_node = tmp_node.next_node
            if hasattr(tmp_node, "prev_node") and tmp_node.prev_node is not None:
                string += "<=>"
            else:
                string += "=>"
            string += str(tmp_node.data)
        return string

if __name__ == "__main__":
    a = Node(4)
    b = Node(a)
    l = DoubleLinkedList().create_from_list([1,2,3,4,7,8])
    l.insert_at_start(1).insert_at_start(5).insert_at_end(6).insert_at_end(7)
    print(l.count)
    print(l)
    l.runner_technique()
    print(l)

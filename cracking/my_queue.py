from __future__ import annotations

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class QueueNode(Generic[T]):
    def __init__(self, item: T, next_node=None) -> None:
        self.item = item
        self.next_node = next_node

    def set_next(self, node: QueueNode):
        self.next_node = node


class MyQueue(Generic[T]):
    def __init__(self) -> None:
        self.first: Optional[QueueNode[T]] = None
        self.last: Optional[QueueNode[T]] = None

    def add(self, item):
        next_node = QueueNode(item)
        if self.first is None or self.last is None:
            self.first = next_node
            self.last = next_node
        else:
            self.last.set_next(next_node)
            self.last = next_node

    def remove(self) -> T:
        assert self.first is not None
        item = self.first.item
        new_first = self.first.next_node
        if new_first is None:
            self.last = None
        self.first = new_first
        return item

    def peek(self) -> T:
        assert self.first is not None
        return self.first.item

    def is_empty(self):
        return self.first is None

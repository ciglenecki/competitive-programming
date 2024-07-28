from __future__ import annotations

from enum import Enum

from cracking.my_queue import MyQueue
from tests.test import Case, test_me


class AnimalEnum(Enum):
    CAT = "cat"
    DOG = "dog"


class Animal:
    timestamp: int

    def __init__(self, type: AnimalEnum) -> None:
        self.type = type

    def __eq__(self, value: Animal) -> bool:
        return self.type == value.type and self.timestamp == value.timestamp


class AnimalQueue:
    def __init__(self) -> None:
        self.dog_queue = MyQueue[Animal]()
        self.cat_queue = MyQueue[Animal]()
        self.timestamp = 0

    def enqueue(self, animal: Animal):
        animal.timestamp = self.timestamp
        if animal.type is AnimalEnum.DOG:
            self.dog_queue.add(animal)
        elif animal.type is AnimalEnum.CAT:
            self.cat_queue.add(animal)
        else:
            raise Exception("Invalid animal type")
        self.timestamp += 1

    def dequeue_any(self):
        if self.dog_queue.is_empty() and self.cat_queue.is_empty():
            raise Exception("All animals are adopted.")
        elif self.dog_queue.is_empty():
            return self.cat_queue.remove()
        elif self.cat_queue.is_empty():
            return self.dog_queue.remove()

        top_dog = self.dog_queue.peek()
        top_cat = self.cat_queue.peek()
        if top_dog.timestamp < top_cat.timestamp:
            return self.dog_queue.remove()
        else:
            return self.cat_queue.remove()

    def dequeue_dog(self):
        return self.dog_queue.remove()

    def dequeue_cat(self):
        return self.cat_queue.remove()


def solution():
    aq = AnimalQueue()
    first_dog = Animal(type=AnimalEnum.DOG)
    first_cat = Animal(type=AnimalEnum.DOG)
    second_cat = Animal(type=AnimalEnum.CAT)
    aq.enqueue(first_cat)
    aq.enqueue(first_dog)
    aq.enqueue(second_cat)
    aq.enqueue(Animal(type=AnimalEnum.DOG))
    aq.enqueue(Animal(type=AnimalEnum.CAT))
    aq.enqueue(Animal(type=AnimalEnum.DOG))
    aq.enqueue(Animal(type=AnimalEnum.DOG))

    assert aq.dequeue_any() == first_cat
    assert aq.dequeue_cat() == second_cat
    assert aq.dequeue_dog() == first_dog
    return


test_cases: list[Case] = [
    {
        "i": (),
        "o": None,
    },
]

test_functions = [solution]

if __name__ == "__main__":
    test_me(test_cases, test_functions)
    test_me(test_cases, test_functions)

from typing import List, Set
from check_test_cases import check_test_cases

test_cases = [
    # todo True
    [[1, 2, 2, 1, 1, 3], False],
    [[1, 2], False],
]

class Solution:
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        memory = {}
        for element in arr:
            if element not in memory:
                memory[element] = 0
            memory[element] += 1

        return len(set(memory.values())) == len(memory)


check_test_cases(Solution.uniqueOccurrences, test_cases)

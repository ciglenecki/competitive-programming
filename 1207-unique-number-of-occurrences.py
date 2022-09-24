from typing import List, Set
from check_test_cases import check_test_cases

test_cases = [
    [[1, 2, 2, 1, 1, 3], True],
    [[1, 2], False],
]

function_name = "uniqueOccurrences"


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memory = {}
        for element in arr:
            if element not in memory:
                memory[element] = 0
            memory[element] += 1

        return len(set(memory.values())) == len(memory)


check_test_cases(getattr(Solution(), function_name), test_cases)

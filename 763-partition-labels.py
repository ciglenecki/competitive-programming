from typing import List, Set

from check_test_cases import check_test_cases

function_name = "partitionLabels"
test_cases = [
    ("ababcbacadefegdehijhklij", [9, 7, 8]),
    ("aaaab", 2),
]


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        result = []
        memory = {}

        for i, character in enumerate(s):

            memory[character] = i

        counter = 0
        current_end = 0

        for i, character in enumerate(s):

            counter += 1

            if memory[character] > current_end:
                current_end = memory[character]

            if i == current_end:
                result.append(counter)
                counter = 0

        return result


check_test_cases(getattr(Solution(), function_name), test_cases)

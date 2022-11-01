from re import I
from typing import List, Set
from check_test_cases import check_test_cases

test_cases = [
    [14, 6],
    [123, 12],
]

function_name = "numberOfSteps"


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        step = 0

        while True:

            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1

            step += 1

            if num == 1:
                return step + 1


check_test_cases(getattr(Solution(), function_name), test_cases)

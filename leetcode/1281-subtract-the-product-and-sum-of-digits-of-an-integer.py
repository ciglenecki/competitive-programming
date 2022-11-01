from os import curdir
from typing import List, Set
from check_test_cases import check_test_cases

test_cases = [
    [234, 15],
    [4421, 21],
]

function_name = "subtractProductAndSum"


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summation = 0
        product = 1

        while True:

            current = n % 10
            n = n // 10

            summation += current
            product *= current

            if n == 0:
                break

        return product - summation


check_test_cases(getattr(Solution(), function_name), test_cases)

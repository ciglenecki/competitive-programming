from typing import List, Set
from check_test_cases import check_test_cases

test_cases = [
    [[1, 2, 2, 1, 1, 3], True],
    [[1, 2], False],
]

function_name = "functionname"

# =============== INSERT SOLUTION HERE

check_test_cases(getattr(Solution(), function_name), test_cases)

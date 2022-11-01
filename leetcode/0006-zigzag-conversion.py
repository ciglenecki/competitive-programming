from check_test_cases import check_test_cases

test_cases = {
    "mamtabbath": "tabbat",
    "bbb": "bbb",
    "bb": "bb",
    "a": "a",
    "ac": "a",
    "babad": "bab",
    "abb": "bb",
    "bba": "bb",
    "aaaa": "aaaa",
    "abba": "abba",
    "abbb": "bbb",
    "aaaaa": "aaaaa",
    "cbbd": "bb",
    "aacdefcaa": "aa",
    "cccccccbbabbddddddd": "ccccccc",
}

function_name = "longestPalindrome"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = [""] * numRows

        row = 0
        is_zigging = False

        for letter in s:

            result[row] += letter

            if is_zigging and row == 0:
                is_zigging = False

            elif not is_zigging and row == numRows - 1:
                is_zigging = True

            if is_zigging:
                row -= 1
            else:
                row += 1

        return "".join(result)


check_test_cases(getattr(Solution(), function_name), test_cases)

from test import Case, test_me

"""
TEXT
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        This is a dutch partitioning problem. We are classifying the array into four groups: red, white, unclassified, and blue. Initially we group all elements into unclassified. We iterate from the beginning as long as the white pointer is less than the blue pointer.

        If the white pointer is red (nums[white] == 0), we swap with the red pointer and move both white and red pointer forward. If the pointer is white (nums[white] == 1), the element is already in correct place, so we don't have to swap, just move the white pointer forward. If the white pointer is blue, we swap with the latest unclassified element.

        2 0 2 1 1 0
        0 0 2 1 1 2
        0 0 1 1 2 2


        """

        RED = 0
        WHITE = 1
        BLUE = 2

        red_idx, white_idx, blue_idx = 0, 0, len(nums) - 1

        while white_idx <= blue_idx:
            element = nums[white_idx]
            if element == RED:
                nums[red_idx], nums[white_idx] = nums[white_idx], nums[red_idx]

                white_idx += 1
                red_idx += 1
            elif element == WHITE:
                white_idx += 1
            else:
                nums[blue_idx], nums[white_idx] = nums[white_idx], nums[blue_idx]
                blue_idx -= 1
        return nums


test_cases: list[Case] = [
    {
        "i": [2, 0, 2, 1, 1, 0],
        "o": [0, 0, 1, 1, 2, 2],
    },
    {
        "i": [2, 0, 1],
        "o": [0, 1, 2],
    },
    {
        "i": [2, 1, 0, 0],
        "o": [0, 0, 1, 2],
    },
]

test_functions = [Solution().sortColors]

if __name__ == "__main__":

    test_me(test_cases, test_functions)

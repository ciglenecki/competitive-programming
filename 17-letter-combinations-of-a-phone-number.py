from typing import List

digits = "23"


class Solution:
    def letterCombinations(self, digits: str):
        if digits == "":
            return []
        phone = [
            ["None"],
            ["None"],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"],
        ]

        list_of_buttons = [phone[int(d)] for d in digits]

        def reduce(list_of_buttons: List[List[str]], results: List[str] = []):
            if len(list_of_buttons) == 0:
                return results

            button = list_of_buttons.pop(0)

            if len(results) > 0:

                return reduce(list_of_buttons, [result + letter for letter in button for result in results])
            else:
                return reduce(list_of_buttons, button)

        res = reduce(list_of_buttons)
        print(res)
        return res

        def solution_a(digits: str):
            if digits == "":
                return []
            phone = [
                None,
                None,
                ["a", "b", "c"],
                ["d", "e", "f"],
                ["g", "h", "i"],
                ["j", "k", "l"],
                ["m", "n", "o"],
                ["p", "q", "r", "s"],
                ["t", "u", "v"],
                ["w", "x", "y", "z"],
            ]

            list_of_digits = [int(d) for d in digits]

            num_of_combinations = 1
            for digit in list_of_digits:
                num_of_combinations *= len(phone[digit])

            accumulated_product = []
            for i, digit in enumerate(list_of_digits):
                if i > 0:
                    accumulated_product.append(accumulated_product[i - 1] / len(phone[digit]))
                else:
                    accumulated_product.append(num_of_combinations / len(phone[digit]))

            result = []
            for i in range(num_of_combinations):
                combination_string = ""
                for idx_digit, digit in enumerate(list_of_digits):
                    real_idx = int((i // accumulated_product[idx_digit]) % len(phone[digit]))
                    combination_string += phone[digit][real_idx]
                result.append(combination_string)
            return result


Solution().letterCombinations(digits)
#         "2345"

#         lists = [phone[int(digit)] for digit in digits]

#         def list_rec(lists, index, result = []):
#             curr_list = lists.pop(0)
#             if result == []:
#                 result = curr_list

#             new_res = []
#             for res in result:
#                 for letter in curr_list:
#                     res.append()5
#             for letter in result:
#                 result.append()


#         list_rec(a)
#         for i in range(len(lists)):
#             curr_list = lists[i]
#             for

#         print([letter for l in lists for letter in l])

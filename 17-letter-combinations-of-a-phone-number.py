from typing import List

digits = "23"


class Solution:
    def letterCombinations(self, digits: str):
        def solution_recursive_reduction(digits: str):
            if digits == "":
                return []
            phone = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"],
            }

            def reduce(button_numbers: List[str], combinations: List[str] = []):
                if len(button_numbers) == 0:
                    return combinations

                button = phone[button_numbers.pop()]

                if len(combinations) > 0:
                    return reduce(
                        button_numbers, [letter + combination for letter in button for combination in combinations]
                    )
                else:
                    return reduce(button_numbers, button)

            return reduce([d for d in digits])

        def solution_b(digits: str):
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

        solution_recursive_reduction(digits)


Solution().letterCombinations(digits)

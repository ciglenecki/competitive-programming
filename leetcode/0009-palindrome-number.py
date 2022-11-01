class Solution:
    def isPalindrome(self, x: int) -> bool:
        def solution_a(x: int):
            """
            Converts x (12321) to a string ('12321')
            Then find the split (middle) index 12(3)21
            Left: 12
            Right: 21
            Check if left is equal to reversed right
            """
            x_str = str(x)
            x_len = len(x_str)
            if x_len == 1:
                return True
            split_index = x_len // 2
            left = x_str[:split_index]
            right = x_str[-split_index:]
            return left == right[::-1]

        def solution_b(x: int):

            # Early return for numbers:
            # -1, -2, ...
            # 10, 100, 110... last digit is 0, number can start with a 0 therefore it's not a polindrome

            if x < 0 or (x % 10 == 0 and x > 0):
                return False

            a = 0
            x_copy = x

            # 12321
            # 1232 1
            # 123 12
            # 12  123
            # 12 == 123 or 12 == 12
            while a < x_copy:
                a = a * 10 + x_copy % 10
                x_copy = x_copy // 10
            return a == x_copy or a // 10 == x_copy

        return solution_b(x)

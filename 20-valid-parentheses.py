class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_dictionary = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        for letter in s:
            if letter == "{" or letter == "(" or letter == "[":
                stack.append(letter)

            if letter in parenthesis_dictionary and (len(stack) == 0 or stack.pop() != parenthesis_dictionary[letter]):
                return False

        return len(stack) == 0


solution = Solution()
sols = {
    "()()[]": True,
    "{[]}": True,
    "{({}())}": True,
    "[[[[{}()[]]]]]": True,
    "{[}]": False,
    "[": False,
    "]": False,
}

results = []
for k, v in sols.items():
    print()
    results.append((k, "Is valid: {}".format(v == solution.isValid(k))))

for item in results:
    print(item)

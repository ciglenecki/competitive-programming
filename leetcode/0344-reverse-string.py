class Solution:
    def reverseString(self, s: List[str]) -> None:

        """
        Do not return anything, modify s in-place instead.
        """

        def non_pythonic(s: List[str]):

            for i in range(len(s) // 2):
                tmp = s[i]
                s[i] = s[len(s) - i - 1]
                s[len(s) - i - 1] = tmp

        def pythonic(s: List[str]):
            for i in range(len(s) // 2):
                s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

        non_pythonic(s)

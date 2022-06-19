class Solution:
    def longestPalindrome(self, s: str):
        def expand_neighbours(left: int, right: int):
            while True:
                if left >= 0 and right < len(s) and s[left] == s[right]:
                    left, right = left - 1, right + 1
                    continue
                return left, right

        best_score = -1
        best_left = 0
        best_right = 1

        for center in range(len(s)):

            left_single, right_single = expand_neighbours(center - 1, center + 1)
            score_single = right_single - left_single

            if score_single > best_score:
                best_left = left_single
                best_right = right_single
                best_score = score_single

            if center + 1 < len(s) and s[center] == s[center + 1]:
                left_pair, right_pair = expand_neighbours(center - 1, center + 2)
                score = right_pair - left_pair

                if right_pair - left_pair > best_score:
                    best_left = left_pair
                    best_right = right_pair
                    best_score = score

        return s[best_left + 1 : best_right]


sols = {
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
}
sol = Solution()
all_right = []
for k, v in sols.items():
    solu = sol.longestPalindrome(k)
    all_right.append(solu == v)
print(all_right)

from test import test_me

"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def string_compare(string: str) -> str:
    if len(string) == 0:
        return string

    char_list = list(string)
    compressed = []
    tmp_char = char_list[0]
    counter = 0

    for i, char in enumerate(char_list):
        if char == tmp_char:
            counter += 1
        else:
            compressed.append(tmp_char)
            compressed.append(str(counter))
            tmp_char = char
            counter = 1

    compressed.append(tmp_char)
    compressed.append(str(counter))

    compressed_string = "".join(compressed)
    if len(compressed_string) < len(string):
        return compressed_string

    return string


test_cases = [
    {
        "i": "aabcccccaaa",
        "o": "a2b1c5a3",
    },
    {
        "i": "abcd",
        "o": "abcd",
    },
    {
        "i": "aaaaaaaaaab",
        "o": "a10b1",
    },
]

test_functions = [
    string_compare,
]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

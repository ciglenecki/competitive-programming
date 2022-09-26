import time
from test import test_me

# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)


def urlify_pythonic(string: str, str_len: int):
    return string[:str_len].replace(" ", "%20")


def urlify_algo(string: str, str_len: int):

    char_list = list(string)
    space_char = "%20"
    space_char_len = len(space_char)
    offset_index = len(char_list) - 1

    for i in range(str_len):
        i = str_len - 1 - i
        character = char_list[i]

        if character == " ":
            char_list[offset_index - space_char_len + 1 : offset_index + 1] = space_char
            offset_index -= space_char_len
        else:
            char_list[offset_index] = char_list[i]
            offset_index -= 1
    return "".join(char_list)

test_cases = (
    (("Mr John Smith    ", 13), "Mr John Smith   ".rstrip().replace(" ", "%20")),
    (("abc e d    ", 7), "abc e d    ".rstrip().replace(" ", "%20")),
    ((" a b    ", 4), "%20a%20b"),
    ((" a b       ", 5), "%20a%20b%20"),

)

test_functions = [
    urlify_pythonic,
    urlify_algo
]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

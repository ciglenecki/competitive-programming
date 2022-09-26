from textwrap import indent
from test import Case, test_me
import json
import numpy as np

"""
brute force: recreate new matrix by switching incides

n, n = 4

left => up
i = 3
j = 0
left_up(i - n + 1, None) 
left_up(i - n + 1, None)

[1] [5] [6] [7] 					[4] [3] [2] [1]
[2] [ ] [ ] [a] 	==rotate==>		[ ] [ ] [ ] [5]
[3] [ ] [ ] [b] 					[ ] [ ] [ ] [6]
[4] [ ] [ ] [c] 					[c] [b] [a] [7]

[4] [3] [2] [1]
[ ] [ ] [ ] [5]
[ ] [ ] [ ] [6]
[c] [b] [a] [7]

[4] [3] [2] [4] [3]
[ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ]
[c] [b] [a] [c] [b]
[ ] [ ] [ ] [ ] [ ]
[c] [b] [a] [c] [b]

[1   2,  3,  4]
[5,  6,  7,  8]
[a,  b,  c,  d]
[e,  f,  g,  h]
 
[e,  a,  5,  1]
[f,  b,  6,  2]
[g,  c,  7,  3]
[h,  d,  8,  4]

"""


def print_matrix(matrix: list[list[int]]):
    for m in matrix:
        for n in m:
            print("{0: <3}".format(n), sep="", end="")
        print()
    print()


def rotate(matrix: list[list[int]]) -> list[list[int]]:

    n = len(matrix)

    for layer in range(int(n / 2)):
        layer_end = n - layer - 1

        for i in range(layer, layer_end):

            offset = i - layer
            tmp_top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[layer_end - offset][layer]

            # bottom -> left
            matrix[layer_end - offset][layer] = matrix[layer_end][layer_end - offset]

            # right -> bottom
            matrix[layer_end][layer_end - offset] = matrix[i][layer_end]

            # top -> right
            matrix[i][layer_end] = tmp_top

    return matrix


random_matrix = np.random.randint(0, 10, size=(6, 6))
test_cases: list[Case] = [
    {
        "i": [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            ["a", "b", "c", "d"],
            ["e", "f", "g", "h"],
        ],
        "o": [
            ["e", "a", 5, 1],
            ["f", "b", 6, 2],
            ["g", "c", 7, 3],
            ["h", "d", 8, 4],
        ],
    },
    {
        "i": random_matrix.tolist(),
        "o": np.rot90(random_matrix, k=3).tolist(),  # cw rotation
    },
]

test_functions = [
    rotate,
]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

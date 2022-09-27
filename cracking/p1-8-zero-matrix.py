from test import Case, test_me


def print_matrix(matrix: list[list[int]]):
    for m in matrix:
        for n in m:
            print("{0: <3}".format(n), sep="", end="")
        print()
    print()


def set_indices(matrix: list[list[int]], seen: dict, element_row: int, element_col: int, num_rows: int, num_cols: int):

    seen[(element_row, element_col)] = True

    for i in range(num_rows):
        if (i, element_col) in seen:
            continue

        if matrix[i][element_col] == 0:
            set_indices(matrix, seen, i, element_col, num_rows, num_cols)
        else:
            seen[(i, element_col)] = True
            matrix[i][element_col] = 0

    for j in range(num_cols):
        if (element_row, j) in seen:
            continue

        if matrix[element_row][j] == 0:
            set_indices(matrix, seen, element_row, j, num_rows, num_cols)
        else:
            seen[(element_row, j)] = True
            matrix[element_row][j] = 0

def zero_matrix_recursion(matrix: list[list[int]]) -> list[list[int]]:

    if len(matrix) == 0:
        return -1
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    seen = {}
    
    for i in range(num_rows):
        for j in range(num_cols):
            if (i,j) not in seen and matrix[i][j] == 0:
                set_indices(matrix, seen, i, j, num_rows,num_cols)
    return matrix


def set_row(matrix: list[list[int]], i: int, value = 0):
    num_cols = len(matrix[0])
    for j in range(num_cols):
        matrix[i][j] = value

def set_col(matrix: list[list[int]], j: int, value = 0):
    num_rows = len(matrix)
    for i in range(num_rows):
        matrix[i][j] = value

def zero_matrix_small_storage(matrix: list[list[int]]) -> list[list[int]]:
    """
    1 0 1
    1 0 1
    1 1 1

    first_row_has_zero = True

    1 0 1
    0 0 1
    1 1 1
    
    """
    
    if len(matrix) == 0:
        return -1
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    first_row_has_zero = False
    first_col_has_zero = False

    # set the flags if first row/col contains a zero because this row/col will be used as a storage
    for j in range(num_cols):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            break

    for i in range(num_rows):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break

    # set zero the 0th row/col anywhere where there's a corresponing 0 in the matrix
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # set the whole row to 0 anywhere where there's a 0 on the 0th row
    for i in range(1, num_rows):
        if matrix[i][0] == 0:
            set_row(matrix, i, 0)

    # set the whole col to 0 anywhere where there's a 0 on the 0th col
    for j in range(1, num_cols):
        if matrix[0][j] == 0:
            set_col(matrix, j, 0)
    
    # if row/col contained a 0 from before set the whole 0th row/col to 0
    if first_row_has_zero:
        set_row(matrix, 0, 0)

    if first_col_has_zero:
        set_col(matrix, 0, 0)

    return matrix



test_cases: list[Case] = [
    {
        "i": [[1,1,1]],
        "o": [[1,1,1]]
    },
    {
        "i": [[1,0,0,1]],
        "o": [[0,0,0,0]]
    },
    {
        "i": [
            [0, 1, 0],
            [2, 3, 4],
            [2, 3, 4],
        ],
        "o": [
            [0, 0, 0],
            [0, 3, 0],
            [0, 3, 0],
        ],
    },
    {
        "i": [
            [0, 1, 0],
            [2, 3, 4],
            [2, 0, 0],
        ],
        "o": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
    },
    {
        "i": [
            [1, 1, 0],
            [2, 3, 4],
            [2, 0, 0],
        ],
        "o": [
            [0, 0, 0],
            [2, 0, 0],
            [0, 0, 0],
        ],
    },
]

test_functions = [
    zero_matrix_recursion,
    zero_matrix_small_storage,
]

if __name__ == "__main__":
    test_me(test_cases, test_functions)

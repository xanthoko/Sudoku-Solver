from setter import get_sudoku_array
from visualiser import print_sudoku


def get_legal_values(sudoku, row, col):
    """Calculates the legal values for the given tile.

    Args:
        sudoku (numpy.array): The sudoku array
        row (integer): The index of the target row
        col (integer): The index of the target column
    Returns:
        list: The available values for the given tile
    """
    # all possible digits
    total_range = list(range(1, 10))

    # restricted values
    row_values = list(sudoku[row, :])
    col_values = list(sudoku[:, col])

    square_r_index = row // 3
    square_c_index = col // 3
    square_r_range = (square_r_index * 3, (square_r_index + 1) * 3)
    square_c_range = (square_c_index * 3, (square_c_index + 1) * 3)
    sqaure = sudoku[square_r_range[0]:square_r_range[1], square_c_range[0]:
                    square_c_range[1]]
    flat_square = list(sqaure.flatten())

    # the set of values that are not availabe
    restricted_values = list(set(row_values + col_values + flat_square))

    # available values = total - restricted
    availabe_values = [x for x in total_range if x not in restricted_values]

    return availabe_values


def recursion_solve(sudoku, r_ind, c_ind):
    if sudoku[r_ind, c_ind]:
        # tile already filled
        next_c = c_ind
        next_r = r_ind
        if c_ind < 8:
            next_c += 1
        else:
            next_r += 1
            next_c = 0

        # recursion call
        ret = recursion_solve(sudoku, next_r, next_c)
        return ret

    availabe_values = get_legal_values(sudoku, r_ind, c_ind)

    if not availabe_values:
        return None

    fake_sudoku = sudoku.copy()
    for value in availabe_values:
        # fill the current position
        fake_sudoku[r_ind, c_ind] = value
        # get the next position
        next_c = c_ind
        next_r = r_ind
        if c_ind < 8:
            next_c += 1
        else:
            next_r += 1
            next_c = 0

        if next_r > 8 or next_c > 8:
            return fake_sudoku

        # recursion call
        ret = recursion_solve(fake_sudoku, next_r, next_c)

        if ret is None:
            continue
        else:
            return ret


sudoku = get_sudoku_array()
print('Original...')
print_sudoku(sudoku)

solved = recursion_solve(sudoku, 0, 0)

print('Solved...')
print_sudoku(solved)

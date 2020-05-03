from collections import OrderedDict

from setter import get_sudoku_array


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
    # if row == 0 and col == 6:
    #     print(sudoku)
    #     print(restricted_values)

    # available values = total - restricted
    availabe_values = [x for x in total_range if x not in restricted_values]

    return availabe_values


def recursion_solve(sudoku, r_ind, c_ind):
    if sudoku[r_ind, c_ind]:
        next_c = c_ind
        next_r = r_ind
        if c_ind < 8:
            next_c += 1
        else:
            next_r += 1
            next_c = 0

        # recursion call
        ret = recursion_solve(sudoku, next_r, next_c)
        # already filled
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


def solve():
    sudoku = get_sudoku_array()

    history = OrderedDict()
    counter = 0

    r_ind = 0
    c_ind = 0
    while True:
        sudoku_value = sudoku[r_ind, c_ind]

        if not sudoku_value:
            try:
                availabe_values = history[(r_ind, c_ind)]
            except KeyError:
                # KeyError: newly visited tile
                availabe_values = get_legal_values(sudoku, r_ind, c_ind)

            if availabe_values:
                # fill the tile
                sudoku[r_ind, c_ind] = availabe_values.pop(0)
                # update availability dict
                history[(r_ind, c_ind)] = availabe_values
            else:
                print('No available values in {},{}'.format(r_ind, c_ind))
                # get the last filled tile and replace its value with the next
                # available one
                latest_filled = next(reversed(history))
                # erase the filled value, NOTE: is this neccessary?
                sudoku[latest_filled] = 0
                latest_available = history[latest_filled]

                if not latest_available:
                    del history[latest_filled]
                    latest_filled = next(reversed(history))

                r_ind, c_ind = latest_filled
                counter += 1
                if counter == 9:
                    print(r_ind, c_ind)
                    print(sudoku)
                    break
                continue

        if c_ind < 8:
            c_ind += 1
        else:
            if r_ind == 8:
                # the end, do what?
                break
            r_ind += 1
            c_ind = 0

    # print('Done')
    # print(sudoku)
    print(history)


# solve()
sudoku = get_sudoku_array()
d = recursion_solve(sudoku, 0, 0)
print(d)

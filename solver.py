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
    # the set of values that are not availabe
    restricted_set = set()
    [restricted_set.add(x) for x in row_values + col_values]
    # available values = total - restricted
    availabe_values = [x for x in total_range if x not in restricted_set]

    # TODO: check the square restriction

    return availabe_values


def solve():
    sudoku = get_sudoku_array()

    history = OrderedDict()

    r_ind = 0
    c_ind = 0
    while True:
        sudoku_value = sudoku[r_ind, c_ind]

        if not sudoku_value:
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
                print(sudoku)
                print(latest_available)
                # continue
                break

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


solve()

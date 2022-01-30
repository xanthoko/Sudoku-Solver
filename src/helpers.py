import time
from typing import Any
from typing import Callable

import numpy


def print_board(board: numpy.ndarray) -> None:
    print()
    for ind, row in enumerate(board):
        if not ind:
            print('- ' * 13)

        new_row = list(row)
        new_row.insert(3, '|')
        # 3 + 3 + 1 cause '|' has been inserted
        new_row.insert(7, '|')
        str_row = list(map(lambda x: str(x), new_row))
        formated_row = ' '.join(str_row)
        formated_row = '| ' + formated_row + ' |'
        print(formated_row)
        if ind in [2, 5, 8]:
            print('- ' * 13)
    print()


def _check_digits_validity(digits: numpy.ndarray) -> bool:
    """Checks that all the digits are present in given array"""
    return len(set(digits)) == 9


def is_board_valid(board: numpy.ndarray) -> bool:
    try:
        for row in board:
            assert _check_digits_validity(row)

        transposed_board = board.transpose()
        for col in transposed_board:
            assert _check_digits_validity(col)

        # check squares
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = board[row:row + 3, col:col + 3]
                assert _check_digits_validity(square.flatten())

        return True
    except AssertionError:
        return False


def timed(func: Callable) -> Callable:

    def inner(*args: Any, **kwargs: Any) -> None:
        start = time.time()
        func(*args, **kwargs)
        duration = time.time() - start
        print(f'Total time taken: {duration:.3f} secs')

    return inner

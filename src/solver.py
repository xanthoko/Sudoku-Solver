from typing import Set
from typing import Tuple

import numpy
from helpers import is_board_valid
from helpers import print_board
from helpers import timed
from setter import fetch_board


def _get_legal_values(row: int, col: int) -> Set[int]:
    global board
    possilbe_values = set(range(1, 10))

    # restricted values
    row_values = set(board[row, :])
    col_values = set(board[:, col])

    # values inside the 3x3 square
    row_start = row // 3 * 3
    row_end = (row // 3 + 1) * 3
    col_start = col // 3 * 3
    col_end = (col // 3 + 1) * 3
    square = board[row_start:row_end, col_start:col_end]
    square = set(square.flatten())

    restricted_values = row_values | col_values | square

    return possilbe_values - restricted_values


def _get_next(row: int, col: int) -> Tuple[int, int]:
    if col == 8:
        row += 1
        col = -1
    return row, col + 1


def _update_solved() -> None:
    global board, solved
    if solved is None:
        solved = board.copy()


@timed
def parent() -> None:
    return solve(0, 0)


def solve(row: int, col: int) -> None:
    global board, solved

    if row > 8 or col > 8:
        _update_solved()
        return

    if board[row, col]:  # tile already filled, go to next
        next_row, next_col = _get_next(row, col)
        return solve(next_row, next_col)

    for value in _get_legal_values(row, col):
        board[row, col] = value
        next_row, next_col = _get_next(row, col)

        solve(next_row, next_col)
        board[row, col] = 0  # solution failed -> backtrack


def main():
    parent()
    print_board(solved)
    print(f'Valid: {is_board_valid(solved)}')


if __name__ == '__main__':
    board: numpy.ndarray = fetch_board('medium')
    solved: numpy.ndarray = None
    main()

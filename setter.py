import numpy


def get_sudoku_array():
    """Creates the sudoku numpy array.

    A value of 0 indicates that the tile is empty.
    """
    # easy sudoku
    sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 3, 0, 0, 0, 0, 1, 6, 0],
              [0, 6, 7, 0, 3, 5, 0, 0, 4], [6, 0, 8, 1, 2, 0, 9, 0, 0],
              [0, 9, 0, 0, 8, 0, 0, 3, 0], [0, 0, 2, 0, 7, 9, 8, 0, 6],
              [8, 0, 0, 6, 9, 0, 3, 5, 0], [0, 2, 6, 0, 0, 0, 0, 9, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # hard sudoku
    # sudoku = [[4, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 7, 8, 5], [0, 0, 7, 0, 4, 8, 0, 5, 0],
    #           [0, 0, 1, 3, 0, 0, 0, 0, 0], [0, 0, 6, 0, 7, 0, 0, 0, 0],
    #           [8, 6, 0, 0, 0, 0, 9, 0, 3], [7, 0, 0, 0, 0, 5, 0, 6, 2],
    #           [0, 0, 3, 7, 0, 0, 0, 0, 0]]

    # convert to numpy array
    sudoku_array = numpy.array(sudoku)

    return sudoku_array

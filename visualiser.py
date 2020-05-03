def print_sudoku(sudoku):
    """Prints the given sudoku with a clear format.

    Args:
        sudoku (numpy.array): The sudoku
    """
    print()
    for ind, row in enumerate(sudoku):
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


if __name__ == '__main__':
    from setter import get_sudoku_array
    sudoku = get_sudoku_array()
    print_sudoku(sudoku)

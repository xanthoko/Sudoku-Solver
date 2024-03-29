from typing import Optional

import numpy
import requests

DEFAULT_BOARD = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 3, 0, 0, 0, 0, 1, 6, 0],
                 [0, 6, 7, 0, 3, 5, 0, 0, 4], [6, 0, 8, 1, 2, 0, 9, 0, 0],
                 [0, 9, 0, 0, 8, 0, 0, 3, 0], [0, 0, 2, 0, 7, 9, 8, 0, 6],
                 [8, 0, 0, 6, 9, 0, 3, 5, 0], [0, 2, 6, 0, 0, 0, 0, 9, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def fetch_board(difficulty: Optional[str] = 'easy') -> numpy.ndarray:
    url = f'https://sugoku.herokuapp.com/board?difficulty={difficulty}'
    resp = requests.get(url)

    if resp.status_code == 200:
        json_resp = resp.json()
        board = json_resp.get('board', DEFAULT_BOARD)
    else:
        board = DEFAULT_BOARD

    return numpy.array(board)

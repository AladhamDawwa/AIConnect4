import random
import time

from board import Board


def AI(difficulty, algorithm):

    board = Board()
    game_end = False

    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        col = random.randint(0, 6)

        board.select_column(col)
        time.sleep(2)

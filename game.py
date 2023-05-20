import random
import time

from AI import playAlphaBeta, playMinimax
from board import Board


def main(difficulty, algorithm):

    board = Board()
    game_end = False

    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        if algorithm == "Minimax":
            col = playMinimax(game_board, difficulty)
        elif algorithm == "Alpha-Beta pruning":
            col = playAlphaBeta(game_board, difficulty + 2)
        else:
            col = random.randint(0, 6)

        board.select_column(col)
        time.sleep(2)

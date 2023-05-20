import math
import random
import copy

ROWS = 6
COLUMNS = 7

PLAYER_PIECE = 2  # "B"
AI_PIECE = 1  # "R"
EMPTY = 0  # "*"


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == board[r][c + 1] == board[r][c + 2] == board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == board[r + 1][c] == board[r + 2][c] == board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == board[r - 1][c + 1] == board[r - 2][c + 2] == board[r - 3][c + 3] == piece:
                return True


def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0


def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[ROWS - r - 1][col] == EMPTY:
            return ROWS - r - 1


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMNS):
        if board[0][col] == EMPTY:
            valid_locations.append(col)
    return valid_locations


def getScore(window, piece):
    score = 0

    if window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5

    if window.count(PLAYER_PIECE) == 3 and window.count(EMPTY) == 1:
        score -= 80

    return score
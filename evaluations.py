from board import *
import math
import random


def evaluation0():
    return random.randint(-100, 100)


def evaluation1(board, piece):
    opponent_piece = 1
    if piece == 1:
        opponent_piece = 2

    piece_fours = evaluation1_scan_util(board, piece, 4)
    piece_threes = evaluation1_scan_util(board, piece, 3)
    piece_twos = evaluation1_scan_util(board, piece, 2)
    opponent_fours = evaluation1_scan_util(board, opponent_piece, 4)
    opponent_threes = evaluation1_scan_util(board, opponent_piece, 3)
    opponent_twos = evaluation1_scan_util(board, opponent_piece, 2)

    utility = (1000 * piece_fours + 5 * piece_threes + 2 * piece_twos) - (
            1000 * opponent_fours + 5 * opponent_threes + 2 * opponent_twos)
    return utility


def evaluation2(board, piece):
    window_length = 4
    score = 0

    ## Score center column
    center_array = [int(i) for i in list(board.board[:, board.columns // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Horizontal
    for r in range(board.rows):
        row_array = [int(i) for i in list(board.board[r, :])]
        for c in range(board.columns - 3):
            window = row_array[c:c + window_length]
            score += evaluate_window(window, piece)

    ## Score Vertical
    for c in range(board.columns):
        col_array = [int(i) for i in list(board.board[:, c])]
        for r in range(board.rows - 3):
            window = col_array[r:r + window_length]
            score += evaluate_window(window, piece)

    ## Score positive sloped diagonal
    for r in range(board.rows - 3):
        for c in range(board.columns - 3):
            window = [board.board[r + i][c + i] for i in range(window_length)]
            score += evaluate_window(window, piece)

    for r in range(board.rows - 3):
        for c in range(board.columns - 3):
            window = [board.board[r + 3 - i][c + i] for i in range(window_length)]
            score += evaluate_window(window, piece)

    return score


def evaluate_window(window, piece):
    score = 0
    opponent_piece = 1
    if piece == 1:
        opponent_piece = 2

    if window.count(piece) == 4 and window.count(0) == 0:
        score += 1000
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opponent_piece) == 4 and window.count(0) == 0:
        score -= 1000
    elif window.count(opponent_piece) == 3 and window.count(0) == 1:
        score -= 5
    elif window.count(opponent_piece) == 2 and window.count(0) == 2:
        score -= 2
    return score


def evaluation1_scan_util(board, piece, number_of_piece):
    count = 0
    for i in range(board.rows):
        for j in range(board.columns):
            if board.board[i][j] == piece:
                count += vertical_scan(i, j, board, number_of_piece)
                count += horizontal_scan(i, j, board, number_of_piece)
                count += diagonal_scan(i, j, board, number_of_piece)
    return count


def vertical_scan(row, column, board, number_of_piece):
    c = 0
    for i in range(row, board.rows):
        if board.board[i][column] == board.board[row][column]:
            c += 1
        else:
            break
    if c >= number_of_piece:
        return 1
    else:
        return 0


def horizontal_scan(row, column, board, number_of_piece):
    c = 0
    for j in range(column, board.columns):
        if board.board[row][j] == board.board[row][column]:
            c += 1
        else:
            break
    if c >= number_of_piece:
        return 1
    else:
        return 0


def diagonal_scan(row, column, board, number_of_piece):
    total = 0
    count = 0
    j = column
    for i in range(row, 6):
        if j > 6:
            break
        elif board.board[i][j] == board.board[row][column]:
            count += 1
        else:
            break
        j += 1
    if count >= number_of_piece:
        total += 1
    count = 0
    j = column
    for i in range(row, -1, -1):
        if j > 6:
            break
        elif board.board[i][j] == board.board[row][column]:
            count += 1
        else:
            break
        j += 1
    if count >= number_of_piece:
        total += 1
    return total

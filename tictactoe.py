"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    return "X" if x_count == o_count else "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == None}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if not (0 <= i < 3) or not (0 <= j < 3):
        raise ValueError("Invalid Move: Out of Bounds!")

    if board[i][j] is not None:
        raise ValueError("Invalid Move!")

    new_board = [row.copy() for row in board]
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    if all(cell is not None for row in board for cell in row):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == "X":
        return 1

    elif win == "O":
        return -1
    else:
        return 0

def max_value(board):
    """
    Returns the maximum utility value for the max player (X).
    """
    if terminal(board):
        return utility(board)

    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Returns the minimum utility value for the min player (O).
    """
    if terminal(board):
        return utility(board)

    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        max_eval = float('-inf')
        best_action = None
        for action in actions(board):
            eval = min_value(result(board, action))
            if eval > max_eval:
                max_eval = eval
                best_action = action
        return best_action
    else:  # current_player == O
        min_eval = float('inf')
        best_action = None
        for action in actions(board):
            eval = max_value(result(board, action))
            if eval < min_eval:
                min_eval = eval
                best_action = action
        return best_action

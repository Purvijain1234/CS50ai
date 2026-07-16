"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count == o_count:
        return X
    else:
        return O
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possible = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible.add((i, j))

    return possible

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if action not in actions(board):
        raise Exception("Invalid Action")

    new_board = copy.deepcopy(board)

    i, j = action

    new_board[i][j] = player(board)

    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    lines = []

    lines.extend(board)

    for j in range(3):
        lines.append([
            board[0][j],
            board[1][j],
            board[2][j]
        ])

    lines.append([
        board[0][0],
        board[1][1],
        board[2][2]
    ])

    lines.append([
        board[0][2],
        board[1][1],
        board[2][0]
    ])

    for line in lines:
        if line == [X, X, X]:
            return X

        if line == [O, O, O]:
            return O

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError

def max_value(board):

    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):

    if terminal(board):
        return utility(board)

    v = math.inf

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

        best_score = -math.inf
        best_move = None

        for action in actions(board):

            score = min_value(
                result(board, action)
            )

            if score > best_score:
                best_score = score
                best_move = action

        return best_move

    else:

        best_score = math.inf
        best_move = None

        for action in actions(board):

            score = max_value(
                result(board, action)
            )

            if score < best_score:
                best_score = score
                best_move = action

        return best_move
    
    raise NotImplementedError

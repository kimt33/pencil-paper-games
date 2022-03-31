"""Module for running tic tac toe games."""


class TicTacToeGame:
    """Platform for playing tic tac toe game.

    Attributes
    ----------
    player1_positions : set of 2-tuple of int
        Positions that player 1 occupies.
    player2_positions : set of 2-tuple of int
        Positions that player 2 occupies.
    avail_positions : tuple
        Positions available to be occupied.
    next_player : int
        Player that will move next.

    Methods
    -------
    __init__(self)
        Initialize game.
    make_move(self, coords)
        Apply piece for player designated by `next_player`

    """
    # NOTE: should the game stop condition be implemented here?
    def __init__(self):
        self.player1_positions = set([])
        self.player2_positions = set([])
        self.avail_positions = {(i, j) for i in range(3) for j in range(3)}
        self.next_player = 1

    def make_move(self, coords):
        pass

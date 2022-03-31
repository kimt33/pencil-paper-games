"""Module for running tic tac toe games."""
import base


# TODO: undo? log?
class TicTacToeGame(base.SinglePiecePlacementGame):
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
        If `0` then player 1. If `1` then player 2.
    status : int
        Status of the game.
        If `0`, then game is on going.
        If `1`, then game is tied.
        If `2`, then player 1 wins.
        If `3`, then player 2 wins.

    Methods
    -------
    __init__(self)
        Initialize game.
    make_move(self, coords)
        Apply piece for player designated by `next_player`

    """
    # NOTE: should the game stop condition be implemented here?
    def __init__(self):
        """Initialize game."""
        super().__init__(num_players=2, board_dimension=(3, 3))

    @property
    def player1_positions(self):
        """Return current occupied positions of player 1 (index 0)."""
        return self.occ_positions[0]

    @property
    def player2_positions(self):
        """Return current occupied positions of player 2 (index 1)."""
        return self.occ_positions[1]

    def make_move(self, coords):
        """Make move for the current player.

        Parameters
        ----------
        coords : 2-tuple of int
            Coordinate on the board.
            0-indexed, where 0 corresponds to the bottom left corner (from player 1's perspective).

        Raises
        ------
        GameError
            If no more moves are available.
            If player 1 won.
            If player 2 won.
            If given position is already occupied.

        """
        coords = tuple(coords)
        if self.status == 1:
            raise base.GameError("Game is tied. There are no more moves available.")
        if self.status == 2:
            raise base.GameError("Game is over. Player 1 won.")
        if self.status == 3:
            raise base.GameError("Game is over. Player 2 won.")

        super().make_move(coords)

    def update_status(self, player_ind):
        """Update game status.

        Parameters
        ----------
        player_ind : int
            Player whose moves will be assessed to check if the game has ended.
            `0` is player 1. `1` is player 2.

        """
        if not self.avail_positions:
            self.status = 1
            return

        positions = self.occ_positions[player_ind]
        # FIXME: a bit wordy
        if (
            all(coords in positions for coords in [(0, 0), (1, 1), (2, 2)]) or
            all(coords in positions for coords in [(0, 2), (1, 1), (2, 0)]) or
            all(coords in positions for coords in [(0, 0), (1, 0), (2, 0)]) or
            all(coords in positions for coords in [(0, 1), (1, 1), (2, 1)]) or
            all(coords in positions for coords in [(0, 2), (1, 2), (2, 2)]) or
            all(coords in positions for coords in [(0, 0), (0, 1), (0, 2)]) or
            all(coords in positions for coords in [(1, 0), (1, 1), (1, 2)]) or
            all(coords in positions for coords in [(2, 0), (2, 1), (2, 2)])
        ):
            self.status = player_ind + 2
        # else:
        #     self.status = 0

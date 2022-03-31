"""Module for running arbitrary game where each player places a single type of piece."""


class GameError(Exception):
    """Error arising from game of tic tac toe."""
    pass


class SinglePiecePlacementGame:
    """Base class for game where each player takes turns placing a single type of game piece.

    Attributes
    ----------
    occ_positions : list of set of 2-tuple of int
        Positions that each player occupies.
    avail_positions : tuple
        Positions available to be occupied.
    num_players : int
        Number of players playing the game.
    next_player : int
        Index of the player that will move next.
    status : int
        Status of the game.
        If `0`, then game is on going.
        If `1`, then game has stopped.

    Methods
    -------
    __init__(self)
        Initialize game.
    make_move(self, coords)
        Apply piece for player designated by `next_player`.
    update_status(self, player_ind)
        Update game status.

    """
    def __init__(self, num_players=2, board_dimension=(3, 3)):
        """Initialize game.

        Parameters
        ----------
        num_players : int
            Number of players.
        board_dimension : 2-tuple of int
            Dimension of the board

        """
        self.occ_positions = [set([]) for i in range(num_players)]
        self.avail_positions = {
            (i, j) for i in range(board_dimension[0]) for j in range(board_dimension[1])
        }
        self.next_player = 0
        self.num_players = num_players
        self.status = 0

    def make_move(self, coords):
        """Make move for the current player.

        Parameters
        ----------
        coords : 2-tuple of int
            Coordinate on the board.
            0-indexed, where 0 corresponds to the bottom left corner (from first player's
            perspective).

        Raises
        ------
        GameError
            If game has stopped.
            If given position is already occupied.

        """
        coords = tuple(coords)
        if self.status == 1:
            raise GameError("Game has stopped.")
        if coords not in self.avail_positions:
            raise GameError("Given position is already occupied.")

        self.occ_positions[self.next_player].add(coords)
        self.update_status(self.next_player)
        self.avail_positions.remove(coords)
        self.next_player = (self.next_player + 1) % self.num_players

    def update_status(self, player_ind):
        """Update game status.

        Parameters
        ----------
        player_ind : int
            Index of the player whose moves will be assessed to check if the game has ended.

        """
        if not self.avail_positions:
            self.status = 1

"""Test tiktactoe module."""
import pytest
import tictactoe


def test_init():
    """Test tictactoe.__init__."""
    game = tictactoe.TicTacToeGame()
    assert game.player1_positions == set([])
    assert game.player2_positions == set([])
    assert game.avail_positions == set(
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    )
    assert game.next_player == 0
    assert game.status == 0


def test_make_move():
    """Test tictactoe.make_move."""
    game = tictactoe.TicTacToeGame()

    game.make_move((0, 0))
    assert game.player1_positions == set([(0, 0)])
    assert game.next_player == 1

    game.make_move((0, 1))
    assert game.player2_positions == set([(0, 1)])
    assert game.next_player == 0

    game.make_move((1, 0))
    assert game.player1_positions == set([(0, 0), (1, 0)])
    assert game.next_player == 1

    with pytest.raises(tictactoe.GameError):
        game.make_move((1, 0))
    assert game.player2_positions == set([(0, 1)])
    game.make_move((1, 1))
    assert game.player2_positions == set([(0, 1), (1, 1)])
    assert game.next_player == 0

    game.make_move((2, 0))
    assert game.player1_positions == set([(0, 0), (1, 0), (2, 0)])
    assert game.next_player == 1

    with pytest.raises(tictactoe.GameError):
        game.make_move((2, 1))
    assert game.status == 2

    # repeat game
    game = tictactoe.TicTacToeGame()

    game.make_move((0, 0))
    assert game.player1_positions == set([(0, 0)])
    assert game.next_player == 1

    game.make_move((0, 1))
    assert game.player2_positions == set([(0, 1)])
    assert game.next_player == 0

    game.make_move((1, 0))
    assert game.player1_positions == set([(0, 0), (1, 0)])
    assert game.next_player == 1

    game.make_move((1, 1))
    assert game.player2_positions == set([(0, 1), (1, 1)])
    assert game.next_player == 0

    game.make_move((2, 2))
    assert game.player1_positions == set([(0, 0), (1, 0), (2, 2)])
    assert game.next_player == 1

    game.make_move((2, 1))
    assert game.player2_positions == set([(0, 1), (1, 1), (2, 1)])
    assert game.next_player == 0

    with pytest.raises(tictactoe.GameError):
        game.make_move((2, 2))
    assert game.status == 3


def test_update_status():
    """Test TicTacToeGame.update_status."""
    game = tictactoe.TicTacToeGame()
    game.avail_positions = set([])
    assert game.status == 0
    game.update_status(0)
    assert game.status == 1

    game = tictactoe.TicTacToeGame()
    game.player1_positions = set([(0, 0), (1, 0), (2, 0)])
    assert game.status == 0
    # NOTE: updating status with the wrong player selected does not change status
    game.update_status(1)
    assert game.status == 0
    game.update_status(0)
    assert game.status == 2

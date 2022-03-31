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
    assert game.next_player == 1

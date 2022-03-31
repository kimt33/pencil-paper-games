"""Test base module."""
import pytest
import base


def test_init():
    """Test SinglePiecePlacementGame.__init__."""
    game = base.SinglePiecePlacementGame(num_players=4, board_dimension=(2, 2))
    assert game.occ_positions == [set([]), set([]), set([]), set([])]
    assert game.avail_positions == set([(0, 0), (0, 1), (1, 0), (1, 1)])
    assert game.next_player == 0
    assert game.num_players == 4
    assert game.status == 0


def test_make_move():
    """Test SinglePiecePlacementGame.make_move."""
    game = base.SinglePiecePlacementGame(num_players=4, board_dimension=(2, 2))

    game.make_move((0, 0))
    assert game.occ_positions[0] == set([(0, 0)])
    assert game.next_player == 1

    game.make_move((0, 1))
    assert game.occ_positions[1] == set([(0, 1)])
    assert game.next_player == 2

    game.make_move((1, 0))
    assert game.occ_positions[2] == set([(1, 0)])
    assert game.next_player == 3

    with pytest.raises(base.GameError):
        game.make_move((1, 0))
    game.make_move((1, 1))
    assert game.occ_positions[3] == set([(1, 1)])
    assert game.next_player == 0


def test_update_status():
    """Test SinglePiecePlacementGame.update_status."""
    game = base.SinglePiecePlacementGame()
    game = base.SinglePiecePlacementGame(num_players=4, board_dimension=(2, 2))
    game.make_move((0, 0))
    game.make_move((0, 1))
    game.make_move((1, 0))
    game.make_move((1, 1))
    assert game.status == 0
    game.update_status(0)
    assert game.status == 1

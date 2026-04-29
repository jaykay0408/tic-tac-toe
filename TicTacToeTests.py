import unittest
from TicTacToeModel import TicTacToeModel, Player


class TestTicTacToeModel(unittest.TestCase):

    def test_initial_state(self) -> None:
        game = TicTacToeModel()
        self.assertFalse(game.is_game_over())
        self.assertEqual(game.get_next_player(), Player.X)
        self.assertIsNone(game.get_winner())

    def test_valid_moves_switch_players(self) -> None:
        game = TicTacToeModel()
        game.place(0, 0)  # X
        self.assertEqual(game.get_next_player(), Player.O)
        game.place(1, 1)  # O
        self.assertEqual(game.get_next_player(), Player.X)

    def test_win_row(self) -> None:
        game = TicTacToeModel()
        game.place(0, 0)  # X
        game.place(1, 0)  # O
        game.place(0, 1)  # X
        game.place(1, 1)  # O
        game.place(0, 2)  # X wins

        self.assertTrue(game.is_game_over())
        self.assertEqual(game.get_winner(), Player.X)

    def test_invalid_out_of_bounds(self) -> None:
        game = TicTacToeModel()
        with self.assertRaises(ValueError):
            game.place(3, 3)

    def test_invalid_occupied(self) -> None:
        game = TicTacToeModel()
        game.place(0, 0)
        with self.assertRaises(ValueError):
            game.place(0, 0)

    def test_no_moves_after_game_over(self) -> None:
        game = TicTacToeModel()
        game.place(0, 0)  # X
        game.place(1, 0)  # O
        game.place(0, 1)  # X
        game.place(1, 1)  # O
        game.place(0, 2)  # X wins

        with self.assertRaises(ValueError):
            game.place(2, 2)


if __name__ == "__main__":
    unittest.main()
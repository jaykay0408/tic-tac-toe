from __future__ import annotations
from typing import Optional
from TicTacToeModel import TicTacToeModel
from TicTacToeView import TicTacToeView
#from TicTacToeViewGUI import TicTacToeViewGUI as TicTacToeView


class TicTacToeController:
    """Controller: handles user input and coordinates model + view."""

    def __init__(self, model: TicTacToeModel, view: TicTacToeView) -> None:
        self._model = model
        self._view = view

    def _get_move(self) -> Optional[tuple[int, int]]:
        """Ask user for a move. Return (row, col) or None to quit."""
        raw = input("Enter move as 'row col' (or 'q' to quit): ").strip()
        pass
    

    def play_game(self) -> None:
        """Main game loop."""
        while not self._model.is_game_over():
            self._view.render_board(self._model.get_board())
            self._view.render_status(self._model)

            move = self._get_move()
            if move is None:
                print("Quitting game.")
                return

            row, col = move
            try:
                self._model.place(row, col)
            except ValueError as e:
                print(f"Invalid move: {e}")

        # Final board + status
        self._view.render_board(self._model.get_board())
        self._view.render_status(self._model)


if __name__ == "__main__":
    model = TicTacToeModel(size=3)
    view = TicTacToeView()
    controller = TicTacToeController(model, view)
    controller.play_game()
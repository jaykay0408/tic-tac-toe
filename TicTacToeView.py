from __future__ import annotations
from typing import Optional, List
from TicTacToeModel import Player, TicTacToeModel


class TicTacToeView:
    """View: responsible only for displaying the game state in text form."""

    def render_board(self, board: List[List[Optional[Player]]]) -> None:
        size = len(board)
        pass
    

    def render_status(self, model: TicTacToeModel) -> None:
        if model.is_game_over():
            winner = model.get_winner()
            if winner is None:
                print("Game over: It's a draw!")
            else:
                print(f"Game over: {winner.value} wins!")
        else:
            print(f"Next player: {model.get_next_player().value}")
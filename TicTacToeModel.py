from __future__ import annotations
from enum import Enum
from typing import List, Optional


class Player(Enum):
    X = "X"
    O = "O"


class TicTacToeModel:
    """Model: game state + rules for Tic Tac Toe.

    - Does NOT do any input/output.
    - Enforces: turn order, valid positions, no moves after game over.
    """

    def __init__(self, size: int = 3) -> None:
        if size < 1:
            raise ValueError("Board size must be at least 1")
        self._size: int = size
        self._board: List[List[Optional[Player]]] = [
            [None for _ in range(size)] for _ in range(size)
        ]
        self._next_player: Player = Player.X
        self._game_over: bool = False
        self._winner: Optional[Player] = None

    # ---------- Public API ----------

    def place(self, row: int, col: int) -> None:
        """Place the current player's mark at (row, col).

        Raises:
            ValueError: if the move is invalid (out of bounds, occupied,
                        or game already over).
        """
        if self._game_over:
            raise ValueError("Game is already over")

        if not (0 <= row < self._size and 0 <= col < self._size):
            raise ValueError("Position out of bounds")

        if self._board[row][col] is not None:
            raise ValueError("Cell is already taken")

        # Place the mark
        self._board[row][col] = self._next_player

        # Check game state
        if self._check_winner(row, col):
            self._game_over = True
            self._winner = self._next_player
        elif self._is_board_full():
            self._game_over = True
            self._winner = None  # Draw
        else:
            # Switch players
            self._next_player = Player.O if self._next_player == Player.X else Player.X

    def get_next_player(self) -> Player:
        """Return the player whose turn it is.

        Raises:
            ValueError: if the game is already over.
        """
        pass

    def is_game_over(self) -> bool:
        pass

    def get_winner(self) -> Optional[Player]:
        """Return the winner, or None if draw or not over yet."""
        pass

    def get_board(self) -> List[List[Optional[Player]]]:
        """Return a *copy* of the board so callers cannot mutate it directly."""
        pass

    def get_size(self) -> int:
        return self._size

    # ---------- Internal helpers ----------

    def _is_board_full(self) -> bool:
        for row in self._board:
            for cell in row:
                if cell is None:
                    return False
        return True

    def _check_winner(self, last_row: int, last_col: int) -> bool:
        """Check if the last move caused a win.

        Only needs to check:
        - That row
        - That column
        - Possibly 2 diagonals
        """
        player = self._board[last_row][last_col]
        if player is None:
            return False

        size = self._size

        # Check row
        if all(self._board[last_row][c] == player for c in range(size)):
            return True

        # Check column
        if all(self._board[r][last_col] == player for r in range(size)):
            return True

        # Check main diagonal
        if last_row == last_col:
            if all(self._board[i][i] == player for i in range(size)):
                return True

        # Check anti-diagonal
        if last_row + last_col == size - 1:
            if all(self._board[i][size - 1 - i] == player for i in range(size)):
                return True

        return False


if __name__ == "__main__":
    # Tiny manual demo of the model only (no UI).
    game = TicTacToeModel()
    game.place(0, 0)  # X
    game.place(1, 0)  # O
    game.place(0, 1)  # X
    game.place(1, 1)  # O
    game.place(0, 2)  # X wins top row

    print("Game over?", game.is_game_over())
    print("Winner:", game.get_winner())
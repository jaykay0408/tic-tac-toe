# TicTacToeViewGUI.py

from __future__ import annotations
from typing import Optional, List

import tkinter as tk

from TicTacToeModel import Player, TicTacToeModel


class TicTacToeViewGUI:
    """
    GUI View for Tic Tac Toe using Tkinter.

    It provides the same public interface as TicTacToeView:
        - render_board(board)
        - render_status(model)

    You can add a call to `view.mainloop()` at the end of your program
    to keep the window open.
    """

    def __init__(self) -> None:
        # Create main window
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Status label at the top
        self.status_label = tk.Label(self.root, text="Welcome to Tic Tac Toe!",
                                     font=("Arial", 14))
        self.status_label.pack(pady=10)

        # Frame that will hold the board cells
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(padx=10, pady=10)

        # Keep references to the label widgets so we can update them
        self._size: int = 0
        self._cell_labels: list[list[tk.Label]] = []

    # ------------------------------------------------------------------
    # Public API used by controller
    # ------------------------------------------------------------------
    def render_board(self, board: List[List[Optional[Player]]]) -> None:
        """Draw or update the board to match the given state."""
        size = len(board)

        # If board size changed, rebuild the grid of labels
        if size != self._size:
            # Clear old widgets
            for child in self.board_frame.winfo_children():
                child.destroy()

            self._cell_labels = []
            for r in range(size):
                row_labels: list[tk.Label] = []
                for c in range(size):
                    lbl = tk.Label(
                        self.board_frame,
                        text="",
                        width=3,
                        height=1,
                        font=("Arial", 24),
                        borderwidth=1,
                        relief="solid",
                    )
                    lbl.grid(row=r, column=c, padx=3, pady=3)
                    row_labels.append(lbl)
                self._cell_labels.append(row_labels)

            self._size = size

        # Update label text according to board contents
        for r in range(size):
            for c in range(size):
                cell = board[r][c]
                text = cell.value if cell is not None else ""
                self._cell_labels[r][c]["text"] = text

        self.root.update_idletasks()

    def render_status(self, model: TicTacToeModel) -> None:
        """Display current game status (whose turn, winner, or draw)."""
        if model.is_game_over():
            winner = model.get_winner()
            if winner is None:
                msg = "Game over: It's a draw!"
            else:
                msg = f"Game over: {winner.value} wins!"
        else:
            msg = f"Next player: {model.get_next_player().value}"

        self.status_label.config(text=msg)
        self.root.update_idletasks()

    # ------------------------------------------------------------------
    # Helper to keep window open (optional)
    # ------------------------------------------------------------------
    def mainloop(self) -> None:
        """Start Tkinter event loop. Call this at the end of your program."""
        self.root.mainloop()


# ----------------------------------------------------------------------
# Simple manual test if you run this file directly
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Very small demo just to see the GUI update; not a full game.
    from TicTacToeModel import TicTacToeModel

    model = TicTacToeModel()
    view = TicTacToeViewGUI()

    # Initial empty board
    view.render_board(model.get_board())
    view.render_status(model)

    # Pretend some moves happened
    model.place(0, 0)  # X
    model.place(1, 1)  # O
    model.place(0, 1)  # X
    model.place(2, 2)  # O
    model.place(0, 2)  # X wins

    view.render_board(model.get_board())
    view.render_status(model)

    view.mainloop()
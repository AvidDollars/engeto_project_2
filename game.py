from dataclasses import dataclass
from operator import itemgetter

from board import Board
from player import Player


@dataclass
class Game:
    _board: Board = Board()
    current_player: Player | None = None

    def is_game_over(self) -> tuple[bool, Player]:
        winning_indices = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (3, 5, 7),
        )

        for indices in winning_indices:
            values = itemgetter(*indices)

            if values(self._board.slots) == (Player.FIRST, Player.FIRST, Player.FIRST):
                return (True, Player.FIRST)

            elif values(self._board.slots) == (
                Player.SECOND,
                Player.SECOND,
                Player.SECOND,
            ):
                return (True, Player.SECOND)

        return (False, Player.MISSING)

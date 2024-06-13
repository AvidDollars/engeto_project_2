from dataclasses import dataclass
from operator import itemgetter

from board import Board
from constants import HR_LINE
from player import Player


@dataclass
class Game:
    """Class representing current state of Tic-Tac-Toe game."""

    _board: Board
    current_player: Player = Player.FIRST

    def __repr__(self) -> str:
        is_game_over, winner = self.is_game_over()

        if not is_game_over:
            return f"{winner}"

        elif is_game_over and winner is None:
            return "It's tie...lol!\nIf you are an optimist, you can say we are both winners."

        return f"{HR_LINE}\nCongratulations, the player {self.current_player} WON!\n{HR_LINE}"

    def is_game_over(self) -> tuple[bool, Player | None]:
        """Evaluates current game status. Return value: tuple[game_is_over, winner]."""

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

        # TIE
        if (
            sum(1 for cell in self._board.slots.values() if isinstance(cell, Player))
            == 9
        ):
            return (True, None)

        return (False, None)

    def play_round(self) -> None:
        """
        Recursively plays a round until player provides either a valid input
        or game is finished.
        """

        prompt = f"{HR_LINE}\n{self.current_player} | Please enter your move number: "
        provided_input = input(prompt)

        insert_succesfull, error_message = self._board.try_insert_player(
            self.current_player, provided_input
        )

        if not insert_succesfull:
            print(error_message)
            self.play_round()
            return

        game_over, _ = self.is_game_over()

        if game_over:
            return

        self.current_player = (
            Player.FIRST if self.current_player == Player.SECOND else Player.SECOND
        )

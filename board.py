from dataclasses import dataclass
from typing import Annotated

from pydantic import Field, validate_call
from tabulate import tabulate

import utils
from player import Player

ValidPosition = Annotated[int, Field(ge=1, le=9)]


@dataclass
class BoardFormatter:
    """Textual representation of Board class."""

    slots: dict[int, Player]

    def __repr__(self) -> str:
        chunks = utils.chunks(list(self.slots.values()), 3)
        return tabulate(chunks, tablefmt="double_grid")


class Board:
    """Class representing Tic-Tac-Toe board."""

    def __init__(
        self,
        slots: dict[int, Player] | None = None,
        board_formatter: BoardFormatter | None = None,
    ):
        if slots is None:
            self.slots = {idx: Player.MISSING for idx in range(1, 10)}
        if board_formatter is None:
            self.board_formatter = BoardFormatter(self.slots)

    def __repr__(self) -> str:
        return repr(self.board_formatter)

    @validate_call
    def insert_player(self, player: Player, position: ValidPosition) -> bool:
        """
        Inserts player into a slot if it is empty and returns True.
        Returns False if slot is already taken.
        """

        if self.is_empty_slot(position):
            self.slots[position] = player
            return True
        return False

    def is_empty_slot(self, position: int) -> bool:
        return True if self.slots[position] == Player.MISSING else False

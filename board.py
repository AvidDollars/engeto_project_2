from dataclasses import dataclass
from functools import cached_property
from typing import Annotated, Literal, MutableMapping

import termcolor
from pydantic import Field
from tabulate import tabulate

import utils
from player import Player

ValidPosition = Annotated[int, Field(ge=1, le=9)]


@dataclass
class BoardFormatter:
    """Textual representation of Board class."""

    slots: MutableMapping[int, Player | int]
    tablefmt: str = "double_grid"
    table_color: Literal["yellow"] = "yellow"

    def __repr__(self) -> str:
        return self.colored_table()

    def colored_table(self) -> str:
        """Returns ANSI colored table."""

        chunks = utils.chunks(list(self.slots.values()), 3)
        table = tabulate(chunks, tablefmt=self.tablefmt)
        table_colored = []

        for character in table:
            if character in self.table_characters:
                table_colored.append(
                    termcolor.colored(character, color=self.table_color)
                )
            elif character == str(Player.FIRST):
                table_colored.append(
                    termcolor.colored(character, color=str(Player.FIRST))  # type: ignore
                )
            elif character == str(Player.SECOND):
                table_colored.append(
                    termcolor.colored(character, color=str(Player.SECOND))  # type: ignore
                )
            else:
                table_colored.append(character)

        return "".join(table_colored)

    @cached_property
    def table_characters(self) -> set[str]:
        """Returns set of characters which are used to construct a table."""

        dummy = (("", ""), ("", ""))  # min is 2x2 grid to have all characters
        table = tabulate(dummy, tablefmt=self.tablefmt)
        return set(character for character in table if character not in (" ", "\n"))


class Board:
    """Class representing Tic-Tac-Toe board."""

    def __init__(
        self,
        slots: MutableMapping[int, Player | int] | None = None,
        board_formatter: BoardFormatter | None = None,
    ):
        if slots is None:
            self.slots: dict[int, Player | int] = {
                idx: idx for idx in (7, 8, 9, 4, 5, 6, 1, 2, 3)
            }
        if board_formatter is None:
            self.board_formatter = BoardFormatter(self.slots)

    def __repr__(self) -> str:
        return repr(self.board_formatter)

    def try_insert_player(
        self, player: Player, position_str: str
    ) -> tuple[bool, str | None]:
        """
        Inserts player into a slot if it is empty. If an insert was successfull, "[True, None]" is returned,
        otherwise "[False, err_msg]" is used as return value. Return value represents "[inserted, optional_err_msg]".
        """

        try:
            position = int(position_str)
        except ValueError:
            return (False, f"'{position_str}' is not valid number.")

        if position < 1 or position > 9:
            return (False, "Not a valid number. Provide a number in range(1, 10)")

        if self._is_empty_slot(position):
            self.slots[position] = player
            return (True, None)
        return (False, f"'{position}' is already taken.")

    def _is_empty_slot(self, position: int) -> bool:
        """Returns boolean whether a slot on board is empty."""

        slot = self.slots[position]
        player_present = Player.FIRST == slot or Player.SECOND == slot
        return True if not player_present else False

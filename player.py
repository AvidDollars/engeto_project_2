from enum import Enum

from termcolor import colored


class Player(Enum):
    """Class representing a player."""

    FIRST = 1
    SECOND = 2

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.value == 1:
            return colored("X", "red")
        elif self.value == 2:
            return colored("O", "light_blue")
        raise NotImplementedError

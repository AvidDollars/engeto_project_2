from enum import Enum


class Player(Enum):
    """Class representing a player. 'MISSING' player represents empty slot on a board."""

    FIRST = 1
    SECOND = 2
    MISSING = 3

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.value == 1:
            return "X"
        elif self.value == 2:
            return "O"
        elif self.value == 3:
            return " "
        raise NotImplementedError

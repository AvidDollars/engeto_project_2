import os
from typing import Iterator, TypeVar

T = TypeVar("T")


def clear_terminal() -> None:
    os.system("cls||clear")


def chunks(values: list[T], size: int) -> Iterator[list[T]]:
    """Yields chunks. Size of a chunk is specified by 'size' argument."""
    for i in range(0, len(values), size):
        yield values[i : i + size]

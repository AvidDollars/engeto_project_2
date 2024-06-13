"""
Second project - Tic Tac Toe

author: Dimitrij Kolničenko
email: dima.kol@seznam.cz
discord: dimitrij_kolnicenko
"""

import inspect

import utils
from board import Board
from constants import HR_LINE
from game import Game


def print_intro_info() -> None:
    print(
        inspect.cleandoc(
            f"""
            Welcome to Tic Tac Toe
            {HR_LINE}
            GAME RULES:
            Each player can place one mark (or stone)
            per turn on the 3x3 grid. The WINNER is
            who succeeds in placing three of their
            marks in a:
            * horizontal,
            * vertical or
            * diagonal row
            {HR_LINE}
            Let's start the game
            """
        )
    )


def init_game() -> tuple[Board, Game]:
    board = Board()
    game = Game(board)
    return (board, game)


def run_game_loop(game: Game, board: Board) -> None:
    print(board)

    while True:
        game.play_round()
        utils.clear_terminal()
        print(board)
        is_game_over, _ = game.is_game_over()

        if is_game_over:
            print(game)
            break


def main() -> None:
    print_intro_info()
    board, game = init_game()
    run_game_loop(game, board)


if __name__ == "__main__":
    main()

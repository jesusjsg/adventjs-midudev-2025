from typing import List, Literal


def move_reno(board: str, moves: str) -> Literal["fail", "crash", "success"]:
    new_board = board.splitlines()
    print(new_board)
    rows = [char for char in new_board]
    return "fail"


if __name__ == "__main__":
    board = """
        .....
        .*# .*
        .@...
        ....."""

    move_reno(board, "D")
    # ➞ 'fail' -> it moves but doesn't pick anything up

    move_reno(board, "U")
    # ➞ 'success' -> it picks something up (*) right above

    move_reno(board, "RU")
    # ➞ 'crash' -> it crashes into an obstacle (#)

    move_reno(board, "RRRUU")
    # ➞ 'success' -> it picks something up (*)

    move_reno(board, "DD")
    # ➞ 'crash' -> it crashes into the bottom of the board

    move_reno(board, "UUU")
    # ➞ 'success' -> it picks something up off the floor (*) and then crashes at the top

    move_reno(board, "RR")
    # ➞ 'fail' -> it moves but doesn't pick anything up

def draw_gift(size: int, symbol: str) -> str:
    box = ""

    if size < 2:
        return box

    for row in range(size):
        if row == 0 or row == size - 1:
            box += symbol * size
        else:
            box += symbol + " " * (size - 2) + symbol

        if row != size - 1:
            box += "\n"

    return box


if __name__ == "__main__":
    print(draw_gift(3, "$"))

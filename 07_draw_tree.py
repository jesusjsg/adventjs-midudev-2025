def draw_tree(height: int, ornament: str, frequency: int) -> str:
    tree_rows = []
    current_position = 1

    for i in range(1, height + 1):
        max_width = 2 * i - 1
        row_chars = []

        for j in range(max_width):
            if current_position % frequency == 0:
                row_chars.append(ornament)
            else:
                row_chars.append("*")
            current_position += 1

        row_str = "".join(row_chars)
        tree_rows.append(row_str)

    base_width = 2 * height - 1
    centered_tree = []

    for row in tree_rows:
        padding = (base_width - len(row)) // 2
        centered_row = " " * padding + row + " " * padding

        centered_tree.append(centered_row.rstrip())

    trunk = "#"
    trunk_padding = (base_width - 1) // 2
    centered_trunk = " " * trunk_padding + trunk

    centered_tree.append(centered_trunk)

    return "\n".join(centered_tree)


if __name__ == "__main__":
    print(draw_tree(5, "o", 2))
    print(draw_tree(3, "@", 3))
    print(draw_tree(4, "+", 1))

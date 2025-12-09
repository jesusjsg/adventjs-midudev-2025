def find_unique_toy(toy: str) -> str:
    char_counts = {}

    for char in toy:
        lower_char = char.lower()
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1

    for char in toy:
        lower_char = char.lower()

        if char_counts[lower_char] == 1:
            return char

    return ""


if __name__ == "__main__":
    print(find_unique_toy("AaBbCc"))
    print(find_unique_toy("abcDEF"))
    print(find_unique_toy("aAaAaAF"))
    print(find_unique_toy("sTreSS"))

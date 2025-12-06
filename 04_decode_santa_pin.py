import re


def decode_santa_pin(code: str) -> str | None:
    codes = re.findall(r"\[(.*?)\]", code)

    if len(codes) < 4:
        return None

    new_code = []
    for pattern in codes:
        if pattern == "<":
            new_code.append(new_code[-1])
            continue

        value = int(pattern[0])
        operation = pattern[1:]

        for operator in operation:
            if operator == "+":
                value = (value + 1) % 10
            elif operator == "-":
                value = (value - 1) % 10
        new_code.append(str(value))

    final_pin = "".join(new_code)

    return final_pin


def decode_santa_pin_no_re(code: str) -> str | None:
    codes = []
    start_index = 0

    while True:
        start_bracket = code.find("[", start_index)
        if start_bracket == -1:
            break

        end_bracket = code.find("]", start_bracket + 1)
        if end_bracket == -1:
            break

        content = code[start_bracket + 1 : end_bracket]
        codes.append(content)
        start_index = end_bracket + 1

    new_code = []
    for pattern in codes:
        if pattern == "<":
            new_code.append(new_code[-1])
            continue

        value = int(pattern[0])
        operation = pattern[1:]

        for operator in operation:
            if operator == "+":
                value = (value + 1) % 10
            elif operator == "-":
                value = (value - 1) % 10
        new_code.append(str(value))

    final_pin = "".join(new_code)

    if (len(final_pin)) < 4:
        return None

    return final_pin


if __name__ == "__main__":
    decode_santa_pin("[1++][2-][3+][<]")
    decode_santa_pin("[9+][0-][4][<]")
    decode_santa_pin("[1+][2-]")

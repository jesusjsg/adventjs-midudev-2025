from typing import List, Dict


def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    color_counts = {}
    for glove in gloves:
        hand = glove.get("hand")
        color = glove.get("color")

        if color not in color_counts:
            color_counts[color] = {"L": 0, "R": 0}

        color_counts[color][hand] += 1

    paired_colors = []
    for color, count in color_counts.items():
        left_hand_count = count.get("L", 0)
        right_hand_count = count.get("R", 0)

        number_pairs = min(left_hand_count, right_hand_count)

        if number_pairs > 0:
            for _ in range(number_pairs):
                paired_colors.append(color)
    return paired_colors


if __name__ == "__main__":
    gloves = [
        {"hand": "L", "color": "red"},
        {"hand": "R", "color": "red"},
        {"hand": "R", "color": "green"},
        {"hand": "L", "color": "blue"},
        {"hand": "L", "color": "green"},
    ]
    print(match_gloves(gloves))  #  ['red', 'green']

gloves2 = [
    {"hand": "L", "color": "gold"},
    {"hand": "R", "color": "gold"},
    {"hand": "L", "color": "gold"},
    {"hand": "L", "color": "gold"},
    {"hand": "R", "color": "gold"},
]

print(match_gloves(gloves2))  # Output: ['gold', 'gold']

gloves3 = [
    {"hand": "L", "color": "red"},
    {"hand": "R", "color": "green"},
    {"hand": "L", "color": "blue"},
]

print(match_gloves(gloves3))  # Output: []

def filter_gifts(gifts: list[str]) -> list[str]:
    list_filter = [c for c in gifts if "#" not in c]
    return list_filter


if __name__ == "__main__":
    print(filter_gifts(["car", "doll#arm", "ball", "#train"]))
    print(filter_gifts([]))

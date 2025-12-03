def manufacture_gifts(gifts_to_produce: list[dict[str, int]]) -> list[str]:
    gifts_produced = []

    for item in gifts_to_produce:
        for _ in range(item["quantity"]):
            gifts_produced.append(item["toy"])
    return gifts_produced

    # This solution is with list comphresion
    # return [item["toy"] for item in gifts_to_produce for _ in range(item["quantity"])]


if __name__ == "__main__":
    production1 = [{"toy": "car", "quantity": 1}, {"toy": "doll", "quantity": 4}]
    print(manufacture_gifts(production1))

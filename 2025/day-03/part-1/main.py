def score(values: list[int]) -> int:
    first = max(values[:-1])
    first_idx = values.index(first)
    second = max(values[first_idx + 1 :])
    return int(first * 10 + second)


if __name__ == "__main__":
    with open("data.in", "r") as infile:
        total = 0
        for line in infile:
            total += score([int(x) for x in line.strip()])
        print(total)

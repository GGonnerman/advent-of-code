# Recursive score function that picks the largest value which will
# still allow you to match the desired length.
def score(values: list[int], desired_length: int) -> int:
    if len(values) == 0 or desired_length == 0:
        return 0

    max_start: int = max(values[: len(values) - desired_length + 1])
    max_start_idx: int = values.index(max_start)

    current: int = max_start * (10 ** (desired_length - 1))
    return current + score(values[max_start_idx + 1 :], desired_length - 1)


if __name__ == "__main__":
    with open("data.in", "r") as infile:
        total = 0
        desired_length = 12
        for line in infile:
            total += score([int(x) for x in line.strip()], desired_length)
        print(total)

from math import floor, log10


def int_len(v):
    return floor(log10(v) + 1)


def gen_table(max_value: int) -> set[int]:
    table: set[int] = set()
    length = int_len(max_value)
    for i in range(1, 10 ** floor(length / 2)):
        res = int("".join(str(i) * 2))
        table.add(res)
    return table


def is_invalid(id, table):
    return id in table


if __name__ == "__main__":
    with open("data.in", "r") as infile:
        total = 0
        peak = 0
        pairs = [tuple(map(int, pair.split("-"))) for pair in infile.read().split(",")]
        for first, second in pairs:
            peak = max(peak, second)

        table = gen_table(peak)

        for first, second in pairs:
            for i in range(first, second + 1):
                if is_invalid(i, table):
                    total += int(i)
        print(total)

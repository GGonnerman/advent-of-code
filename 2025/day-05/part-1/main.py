from typing import NamedTuple


class Range(NamedTuple):
    start: int
    end: int


def is_range(line: str) -> bool:
    return "-" in line


def is_in_any_range(value: int, ranges: list[Range]):
    for range in ranges:
        if value < range.start:
            break
        if value <= range.end:
            return True

    return False


if __name__ == "__main__":
    ranges: list[Range] = []
    with open("data.in", "r") as infile:
        for line in infile:
            if is_range(line):
                start, end = map(int, line.strip().split("-"))
                ranges.append(Range(start, end))
            else:
                break
        ranges.sort()
        count = 0
        for line in infile:
            if is_in_any_range(int(line), ranges):
                count += 1
    print(count)

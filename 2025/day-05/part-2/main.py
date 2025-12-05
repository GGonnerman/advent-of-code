from typing import NamedTuple


class Range(NamedTuple):
    start: int
    end: int


def merge(a: Range, b: Range) -> None | Range:
    if a.end < b.start:
        return None

    c = Range(min(a.start, b.start), max(a.end, b.end))
    return c


if __name__ == "__main__":
    ranges: list[Range] = []
    with open("data.in", "r") as infile:
        # Load all the ranges
        for line in infile:
            if "-" not in line:
                break
            start, end = map(int, line.strip().split("-"))
            ranges.append(Range(start, end))

        ranges.sort()

        # Go through and merge any overlapping ranges together
        # until no ranges can be merged
        i = 0
        while i < len(ranges) - 1:
            current = ranges[i]
            next = ranges[i + 1]
            res = merge(current, next)
            if res is None:
                i += 1
            else:
                ranges[i] = res
                _ = ranges.pop(i + 1)
                i = 0

        # Sum the number of ids in each range
        total = 0
        for segment in ranges:
            total += segment.end - segment.start + 1

        print(total)

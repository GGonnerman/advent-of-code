from functools import reduce
from typing import Callable, TypeVar


T = TypeVar("T")


def rotate(arr: list[list[T]]) -> list[list[T]]:
    out: list[list[T]] = [[] for _ in range(len(arr[0]))]
    for row in arr:
        for i, cell in enumerate(row):
            out[i].append(cell)
    return out


def apply_op(raw_op: str, terms: list[int]):
    op_map: dict[str, Callable[[float, float], float]] = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    op = op_map[raw_op]

    return reduce(op, terms)


def split_into_segments(line: str, split_points: set[int]):
    out: list[str] = []
    accum: str = ""
    for i in range(0, len(line)):
        if i in split_points and i > 0:
            out.append(accum)
            accum = line[i]
        elif (i + 1) in split_points:
            continue
        else:
            accum += line[i]
    if accum != "":
        out.append(accum)
    return out


def collapse_rows(row: list[str]) -> list[int]:
    char_groups: list[list[str]] = rotate([list(cell) for cell in row])
    out: list[int] = []
    for char_group in reversed(char_groups):
        out.append(int("".join(char_group)))
    return out


if __name__ == "__main__":
    with open("data.in", "r") as infile:
        lines = [line.replace("\n", "") for line in infile if line != ""]
        operations: list[str] = []
        split_points: set[int] = set()
        for i, char in enumerate(lines[-1]):
            if char != " ":
                split_points.add(i)
                operations.append(char)

        numbers = [split_into_segments(line, split_points) for line in lines[:-1]]
        numbers = rotate(numbers)
        numbers = [collapse_rows(row) for row in numbers]

        total = 0
        for op, numbers in zip(operations, numbers):
            total += apply_op(op, numbers)
        print(total)

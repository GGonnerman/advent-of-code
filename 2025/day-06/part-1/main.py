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


if __name__ == "__main__":
    with open("data.in", "r") as infile:
        lines = [line.strip() for line in infile if line != ""]
        operations = lines[-1].split()
        numbers = [[int(v) for v in row] for row in [row.split() for row in lines[:-1]]]
        numbers = rotate(numbers)
        total = 0
        for op, numbers in zip(operations, numbers):
            total += apply_op(op, numbers)
        print(total)

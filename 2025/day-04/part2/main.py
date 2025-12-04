def make_grid(lines: list[str]) -> list[list[bool]]:
    out: list[list[bool]] = []
    for line in lines:
        out.append([])
        for char in line.strip():
            out[-1].append(True if char == "@" else False)
    return out


def make_neighbor_grid(original_grid: list[list[bool]]) -> list[list[int]]:
    height = len(original_grid)
    width = len(original_grid[0])
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for h in range(height):
        for w in range(width):
            # Add to neighbors only if this exists
            # print(original_grid[h][w], (h, w))
            if original_grid[h][w]:
                for offset_h in range(-1, 2):
                    for offset_w in range(-1, 2):
                        # print(f"Offsets: ({offset_h}, {offset_w})")
                        if offset_w == 0 and offset_h == 0:
                            continue
                        new_h = h + offset_h
                        new_w = w + offset_w
                        if new_h < 0 or new_w < 0 or new_h >= height or new_w >= width:
                            continue
                        grid[new_h][new_w] += 1
    return grid


def iterate(grid: list[list[bool]]):
    count = 0
    any_removed = True
    while any_removed:
        any_removed = False
        neighbors = make_neighbor_grid(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                paper_cell = grid[i][j]
                neighbor_cell = neighbors[i][j]
                if paper_cell and neighbor_cell < 4:
                    grid[i][j] = False
                    count += 1
                    any_removed = True
    return count


if __name__ == "__main__":
    with open("data.in", "r") as infile:
        grid = make_grid(infile.readlines())
        count = iterate(grid)
        print(count)

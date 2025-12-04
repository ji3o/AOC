from aoc_input_call import get_aoc_input

data = get_aoc_input(2025, 4)

grid = [list(line.strip()) for line in data]

rows = len(grid)
cols = len(grid[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def count_at_neighbors(r, c):
    count = 0
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == "@":
                count += 1
    return count

def count_all_at():
    return sum(
        1
        for r in range(rows)
        for c in range(cols)
        if grid[r][c] == "@"
    )

initial_at_count = count_all_at()

while True:
    to_remove = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            neighbors = count_at_neighbors(r, c)
            if neighbors <= 3:
                to_remove.append((r, c))

    if not to_remove:
        break

    for r, c in to_remove:
        grid[r][c] = "."

remaining_at = count_all_at()

diff = initial_at_count - remaining_at

print("Initial - Remaining):", diff)

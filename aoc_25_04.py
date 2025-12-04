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

valid_at_count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "@":
            continue
        neighbors = count_at_neighbors(r, c)
        if neighbors <= 3:
            valid_at_count += 1

print("'@' with 3 or less neighbours:", valid_at_count)

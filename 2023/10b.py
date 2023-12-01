grid = [list(line) for line in open("10.txt").read().splitlines()]
start_pos = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'S')

connections = {
    (l, (i,j)): ((i, j), r)
    for i, row in enumerate(grid)
    for j, cell in enumerate(row)
    for l, r in (
        [((i+1, j), (i-1, j)), ((i-1, j), (i+1, j))] if cell == "|" else
        [((i, j-1), (i, j+1)), ((i, j+1), (i, j-1))] if cell == "-" else
        [((i, j-1), (i-1, j)), ((i-1, j), (i, j-1))] if cell == "J" else
        [((i+1, j), (i, j+1)), ((i, j+1), (i+1, j))] if cell == "F" else
        [((i, j-1), (i+1, j)), ((i+1, j), (i, j-1))] if cell == "7" else
        [((i-1, j), (i, j+1)), ((i, j+1), (i-1, j))] if cell == "L" else
        []
    )
}

def traverse(previous_pos, current_pos):
    visited = {previous_pos}
    while True:
        visited.add(current_pos)
        previous_pos, current_pos = connections.get((previous_pos, current_pos), (None, None))
        if current_pos is None: raise Exception("Not a loop")
        if grid[current_pos[0]][current_pos[1]] == "S": return visited

visited = traverse(start_pos, (start_pos[0]-1, start_pos[1]))
grid[start_pos[0]][start_pos[1]] = "J"
count, enter_from = 0, ""
for row_idx, row in enumerate(grid):
    is_in = False
    for cell_idx, cell in enumerate(row):
        if (row_idx, cell_idx) in visited:
            if cell == "|": is_in = not is_in
            elif cell == "F": enter_from = "F"
            elif cell == "L": enter_from = "L"
            elif cell == "J": is_in = (is_in if enter_from == "L" else not is_in)
            elif cell == "7": is_in = (is_in if enter_from == "F" else not is_in)
        else: count += is_in
print(count)

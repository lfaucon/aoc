def pp(g):
    print(64*"-")
    for r in g:
        print("".join(map(str,r)))

grid = [list(line) for line in open("10.txt").read().splitlines()]
pp(grid)
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

# print(connections)
def traverse(previous_position, current_position):
    visited = set()
    distance, distances = 0, {}
    while True:
        # print(64*"-")
        # print(previous_position, current_position)
        # print(grid[current_position[0]][current_position[1]])
        previous_position, current_position = connections.get((previous_position, current_position), (None, None))
        distance += 1
        distances[distance] = current_position
        # print(previous_position, current_position)
        if current_position is None:
            return "Not a loop"
        if current_position in visited or grid[current_position[0]][current_position[1]] == "S":
            return "I looped", distances, (distance+1)/2
        visited.add(current_position)

print(traverse(start_pos, (start_pos[0]-1, start_pos[1])))
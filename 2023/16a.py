grid = list(map(list, open("16.txt").read().splitlines()))
for row in grid: print("".join(row))
LEFT, UP, RIGHT, DOWN = (0, -1), (-1, 0), (0, 1), (1, 0)

visited = set()
queue = [((0,0), RIGHT)]
while queue:
    position, direction = queue.pop()
    print("Exploring", position, direction)
    pr, pc = position
    if pr < 0 or pr >= len(grid) or pc < 0 or pc >= len(grid[0]):
        print("Skipping off grid")
        continue
    if (position, direction) in visited:
        print("Skipping already visited")
        continue
    visited.add((position, direction))
    dr, dc = direction
    if grid[pr][pc] == ".":
        queue.append(((pr+dr, pc+dc), direction))
    elif grid[pr][pc] == "|":
        if direction == LEFT or direction == RIGHT:
            queue.append(((pr-1, pc), UP))
            queue.append(((pr+1, pc), DOWN))
        else:
            queue.append(((pr+dr, pc+dc), direction))
    elif grid[pr][pc] == "-":
        if direction == DOWN or direction == UP:
            queue.append(((pr, pc-1), LEFT))
            queue.append(((pr, pc+1), RIGHT))
        else:
            queue.append(((pr+dr, pc+dc), direction))
    elif grid[pr][pc] == "/" or grid[pr][pc] == "\\":
        matches = {
            "/": {DOWN: LEFT, RIGHT: UP, UP: RIGHT, LEFT: DOWN},
            "\\": {DOWN: RIGHT, RIGHT: DOWN, UP: LEFT, LEFT: UP},
        }
        new_direction = matches[grid[pr][pc]][direction]
        dr, dc = new_direction
        queue.append(((pr+dr, pc+dc), new_direction))

print(visited)
print(len(set(position for position, _ in visited)))

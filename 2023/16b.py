grid = list(map(list, open("16.txt").read().splitlines()))
for row in grid: print("".join(row))
LEFT, UP, RIGHT, DOWN = (0, -1), (-1, 0), (0, 1), (1, 0)

def count_energized_tiles(starting_pos, starting_direction):
    visited = set()
    queue = [(starting_pos, starting_direction)]
    while queue:
        position, direction = queue.pop()
        # print("Exploring", position, direction)
        pr, pc = position
        if pr < 0 or pr >= len(grid) or pc < 0 or pc >= len(grid[0]):
            # print("Skipping off grid")
            continue
        if (position, direction) in visited:
            # print("Skipping already visited")
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

    # print(visited)
    return len(set(position for position, _ in visited))

all_energization_counts =  [
    count_energized_tiles(p, d) for p, d in(
        [((0, k), DOWN) for k in range(len(grid[0]))]
        + [((len(grid)-1, k), UP) for k in range(len(grid[0]))]
        + [((k, 0), RIGHT) for k in range(len(grid))]
        + [((k, len(grid[0])-1), LEFT) for k in range(len(grid[0]))]
    )
]

print(all_energization_counts)

print(max(all_energization_counts))
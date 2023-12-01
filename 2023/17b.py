grid = [list(map(int, l)) for l in open("17.txt").read().splitlines()]
print(grid)
nr, nc = len(grid), len(grid[0])

MAX_INT = sum(sum(r) for r in grid)

from queue import PriorityQueue

LEFT, UP, RIGHT, DOWN = (0, -1), (-1, 0), (0, 1), (1, 0)
directions = [LEFT, UP, RIGHT, DOWN]
opposites = {LEFT: RIGHT, RIGHT: LEFT, UP: DOWN, DOWN: UP}


q = PriorityQueue()
shortest_distances = {((0,0), RIGHT, 0): 0}
q.put((0, (0,0), RIGHT, 0))
q.put((0, (0,0), DOWN, 0))
target = (nr-1, nc-1)

while q.not_empty:
    distance, position, current_direction, repeat_count = q.get()
    if position == target and repeat_count >= 4:
        print("Found target at distance", distance)
        exit()

    if distance > shortest_distances.get((position, current_direction, repeat_count), MAX_INT):
        continue

    pr, pc = position
    for new_direction, new_count in [
        (d, (repeat_count+1) if d == current_direction else 1) 
        for d in directions 
        if (d == current_direction or repeat_count >= 4) and (d != current_direction or repeat_count < 10) and d != opposites[current_direction]
    ]:
        dr, dc = new_direction
        new_pr, new_pc = (pr+dr, pc+dc)
        new_position = (new_pr, new_pc)
        if new_pr < 0 or new_pr >= nr or new_pc < 0 or new_pc >= nc:
            continue
        new_distance = distance + grid[new_pr][new_pc]
        if new_distance < shortest_distances.get((new_position, new_direction, new_count), MAX_INT):
            shortest_distances[(new_position, new_direction, new_count)] = new_distance
            q.put((new_distance, new_position, new_direction, new_count))

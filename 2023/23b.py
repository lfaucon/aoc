forest = [list(l) for l in open("23.txt").read().splitlines()]

intersection_points = [
    (r,c)
    for r in range(1, len(forest)-1)
    for c in range(1, len(forest[0])-1)
    if forest[r][c] != "#"
    and sum(forest[_r][_c] == "#" for _r, _c in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]) <= 1
]

START, END = (0,1), (len(forest)-1, len(forest[0])-2)
START_IDX, END_IDX = -1,len(intersection_points)

intersection_points_set = set(intersection_points)

intersection_points_indices = {p:i for i, p in enumerate(intersection_points)}
intersection_points_indices[START] = START_IDX
intersection_points_indices[END] = END_IDX

for ir, ic in intersection_points:
    intersection_map = "\n".join("".join(forest[r][ic-1:ic+2]) for r in range(ir-1, ir+2))
    assert intersection_map.count(".") == 1
    assert forest[ir][ic] == "."
    print(intersection_map)
    print()

def walk(path):
    start = tuple(path)
    visited = set(path)
    while not path[-1] in intersection_points_set and path[-1] != END and path[-1] != START:
        lr, lc = path[-1]
        for nr, nc in [(lr, lc+1), (lr, lc-1), (lr+1, lc), (lr-1, lc)]:
            if forest[nr][nc] != "#" and (nr, nc) != path[-2]:
                if (nr, nc) in visited:
                    raise RuntimeError(f"The path starting in {start} loops at {(nr, nc)}")
                visited.add((nr, nc))
                path.append((nr, nc))
                break
        if path[-1] == (lr, lc):
            raise RuntimeError(f"The path starting in {start} could not continue at {(nr, nc)}")
    return path

connections = {}
for intersection_idx in range(len(intersection_points)):
    print("Computing connections for intersection", intersection_idx)
    ir, ic = intersection_points[intersection_idx]
    for pr, pc in [(ir, ic+1), (ir, ic-1), (ir+1, ic), (ir-1, ic)]:
        if forest[pr][pc] != "#":
            path = walk([(ir, ic), (pr, pc)])
            connections[intersection_idx] = connections.get(intersection_idx, {})
            connections[intersection_idx][intersection_points_indices[path[-1]]] = len(path)-1

first_path = walk([START, (1, 1)])
connections[-1] = { intersection_points_indices[first_path[-1]]: len(first_path)-1 }

print("----------------------------------------")
for idx, point in enumerate(intersection_points):
    print("Point", idx, ":", point)
print("----------------------------------------")
for idx in range(-1, len(connections)):
    print("Connection", idx, ":", connections.get(idx))

queue = [((-1,), 0)]
longest_path = 0
while queue:
    positions, distance = queue.pop()
    if positions[-1] == END_IDX:
        print("Found a path of length:", distance)
        longest_path = max(longest_path, distance)
        continue

    for next_position, distance_increment in connections[positions[-1]].items():
        if next_position not in positions:
            queue.append((positions + (next_position,), distance + distance_increment))

print("Longest path:", longest_path)
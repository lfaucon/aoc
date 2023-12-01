instructions = [l.split(" ") for l in open("18.txt").read().splitlines()]
instructions = [(direction, int(length)) for direction, length, _ in instructions]

path = [(0,0)]
for instruction in instructions:
    direction, length = instruction
    x,y = path[-1]
    moves = [
        (x,y+k) if direction == "R" else
        (x+k,y) if direction == "D" else
        (x,y-k) if direction == "L" else
        (x-k,y) if direction == "U" else
        ()
        for k in range(1, 1+length)
    ]
    path.extend(moves)

###############################################
x_min = min([x for x, _ in path])
x_max = max([x for x, _ in path])
y_min = min([y for _, y in path])
y_max = max([y for _, y in path])

path_set = set(path)
for x in range(x_min, x_max+1):
    for y in range(y_min, y_max+1):
        print("#" if (x,y) in path_set else ".", end="")
    print()

##############################################
out_lava = {(x_min-1, y_min-1)}
queue = [(x_min-1, y_min-1)]
while queue:
    x,y = queue.pop()
    neighbors = [(x+1,y), (x-1,y), (x, y+1), (x,y-1)]
    to_explore = [
        (a,b)
        for a,b in neighbors
        if x_min-2<a<x_max+2
        and y_min-2<b<y_max+2
        and (a,b) not in out_lava
        and (a,b) not in path_set
    ]
    out_lava.update(to_explore)
    queue.extend(to_explore)

enclosed_lava = set()
for x in range(x_min, x_max+1):
    for y in range(y_min, y_max+1):
        if (x,y) not in out_lava:
            enclosed_lava.add((x,y))

print("-----------------------")
for x in range(x_min-2, x_max+3):
    for y in range(y_min-2, y_max+3):
        print("X" if (x,y) in enclosed_lava else "#" if (x,y) in path_set else ".", end="")
    print()

print(len(enclosed_lava))
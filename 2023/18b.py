instructions = [l.split(" ") for l in open("18.txt").read().splitlines()]
instructions = [("RDLU"[int(hexa[-2])], int(hexa[2:-2], 16)) for _, _, hexa in instructions]

path = [(0, 0)]
for instruction in instructions:
    (d, l), (x, y) = instruction, path[-1]
    path.append({"R": (x, y + l), "D": (x + l, y), "L": (x, y - l), "U": (x - l, y)}[d])

area = 0
edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
node_rows = sorted(list(set(x for x, _ in path)))
bands = [(a, a) for a in node_rows]
bands += [(node_rows[idx] + 1, node_rows[idx + 1] - 1) for idx in range(len(node_rows) - 1)]

for a, b in bands:
    crossings = [
        (p1, p2)
        for p1, p2 in sorted(edges, key=lambda e: e[0][1] + e[1][1])
        if p1[0] == a or p2[0] == a or p1[0] > a > p2[0] or p1[0] < a < p2[0]
    ]
    crossing_types = [
        "accross"
        if (p1[0] > a > p2[0] or p1[0] < a < p2[0])
        else "horizontal"
        if (p1[0] == a and p2[0] == a)
        else "down"
        if (p1[0] > a or p2[0] > a)
        else "up"
        for p1, p2 in crossings
    ]
    bounds = []
    current_idx = 0
    while current_idx < len(crossings):
        if crossing_types[current_idx] == "horizontal":
            if crossing_types[current_idx - 1] == crossing_types[current_idx + 1]:
                if len(bounds) % 2 == 0:
                    del bounds[-1]
                    current_idx += 1
            else:
                if len(bounds) % 2 == 0:
                    del bounds[-1]
                else:
                    current_idx += 1
        else:
            bounds.append(crossings[current_idx][0][1])
        current_idx += 1
    area += (b - a + 1) * sum((bounds[k + 1] - bounds[k] + 1) for k in range(0, len(bounds), 2))

print(area)

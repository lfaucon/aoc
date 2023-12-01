seeds, *maps = open("5.txt").read().split("\n\n")
seeds = [int(s) for s in seeds.strip("\n").split(" ") if s.isnumeric()]
seeds_ranges = [(0, seeds[k], seeds[k] + seeds[k + 1] - 1) for k in range(0, len(seeds), 2)]
maps = [[tuple(map(int, line.split(" "))) for line in m.splitlines()[1:]] for m in maps]
locations = set()
while seeds_ranges:
    start_idx, a, b = seeds_ranges.pop()
    for idx in range(start_idx, len(maps)):
        for dest, source, l in maps[idx]:
            if source <= a <= b <= source + l - 1:
                a, b = dest + (a - source), dest + (b - source)
                break
            elif a <= source + l - 1 < b:
                seeds_ranges.append((idx, a, source + l - 1))
                a, b = source + l, b
            elif a < source <= b:
                seeds_ranges.append((idx, source, b))
                a, b = a, source - 1
    locations.update({a, b})
print(min(locations))

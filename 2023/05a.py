seeds, *maps = open("5.txt").read().split("\n\n")
seeds = [int(s) for s in seeds.strip("\n").split(" ") if s.isnumeric()]
parse_map = lambda m: [tuple(map(int, line.split(" "))) for line in m.splitlines()[1:]]
maps = [parse_map(m) for m in maps]
locations = []
for s in seeds:
    loc = s
    for m in maps:
        for dest, source, l in m:
            if source <= loc <= source + l:
                loc = dest + (loc - source)
                break
    locations.append(loc)
print(min(locations))
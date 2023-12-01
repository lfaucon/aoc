instructions, connections = open("8.txt").read().split("\n\n")
connections = {
    line[:3]: {'L': line[7:10], 'R': line[12:15]}
    for line in connections.splitlines()
}
steps = 0

def times_to_Z(n):
    cache = {}
    steps = 0
    while (n, steps%len(instructions)) not in cache:
        cache[(n, steps%len(instructions))] = steps
        n = connections[n][instructions[steps%len(instructions)]]
        steps += 1
    return {c: v for c, v in cache.items() if c[0][-1] == 'Z'}

nodes = [n for n in connections if n[-1] == 'A']
for node in nodes:
    print(times_to_Z(node))
# I don't know why this was possible ...
import math; print(math.lcm(11567, 19637, 15871, 21251, 12643, 19099))

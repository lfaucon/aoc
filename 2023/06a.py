parse_line = lambda l: [int(s) for s in l.split(" ") if s.isnumeric()]
times, distances = map(parse_line, open("6.txt").read().splitlines())
count = lambda t, d: 2 * (1 + int(t/2) - next(k for k in range(t) if k * (t-k) > d)) - (t%2 == 0)
import math; print(math.prod([count(t, d) for t, d in zip(times, distances)]))

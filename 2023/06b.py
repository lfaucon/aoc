parse_line = lambda l: int("".join([s for s in l.split(" ") if s.isnumeric()]))
time, distance = map(parse_line, open("6.txt").read().splitlines())
import math; print(time - 2 * math.ceil((time - (time**2 - 4*distance) ** 0.5) / 2))

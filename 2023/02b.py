games = [line.split(":")[1].split(";") for line in open("2.txt").read().splitlines()]
games = [[o.strip().split(" ") for obs in game for o in obs.split(",")] for game in games]
powers = [{"red": -1, "green": -1, "blue": -1} for _ in games]
for power, game in zip(powers, games):
    for n, color in game: power[color] = max(power[color], int(n))
import math; print(sum(math.prod(power.values()) for power in powers))
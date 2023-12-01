LIMITS = {"red": 12, "green": 13, "blue": 14}
games = [line.split(":")[1].split(";") for line in open("2.txt").read().splitlines()]
games = [[o.strip().split(" ") for obs in game for o in obs.split(",")] for game in games]
print(sum([i+1 for i, game in enumerate(games) if all(int(n) <= LIMITS[c] for n, c in game)]))

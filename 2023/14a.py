grid = [list(l) for l in open("14.txt").read().splitlines()]
load = 0


for r in grid:
    print("".join(r))
print("------------------")

for c_idx in range(len(grid[0])):
    cur_fall_idx = 0
    for r_idx in range(len(grid)):
        if grid[r_idx][c_idx] == "#":
            cur_fall_idx = r_idx + 1
        if grid[r_idx][c_idx] == "O":
            grid[r_idx][c_idx] = grid[cur_fall_idx][c_idx]
            grid[cur_fall_idx][c_idx] = "O"
            cur_fall_idx += 1

for r in grid:
    print("".join(r))
print("------------------")

load = 0
for c_idx in range(len(grid[0])):
    for r_idx in range(len(grid)):
        if grid[r_idx][c_idx] == "O":
            load += len(grid) - r_idx
    # extra_load = stone * (2 * len(grid) - stone + 1) / 2
    # print(stone, extra_load)
    # load += extra_load
print(load)
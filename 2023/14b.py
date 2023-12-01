import numpy as np
grid = np.array([list(l) for l in open("14.txt").read().splitlines()])

def pp(g):
    print("grid of shape", g.shape)
    for r in g:
        print("".join(r))
    print("------------------")

def move_north(g): 
    for c_idx in range(len(g[0])):
        cur_fall_idx = 0
        for r_idx in range(len(g)):
            if g[r_idx][c_idx] == "#":
                cur_fall_idx = r_idx + 1
            if g[r_idx][c_idx] == "O":
                g[r_idx][c_idx] = g[cur_fall_idx][c_idx]
                g[cur_fall_idx][c_idx] = "O"
                cur_fall_idx += 1

def rotate(g):
    return 

def apply_cycle(g):
    # pp(g)
    move_north(g)
    # pp(g)
    g = g.T
    move_north(g)
    # pp(g.T)
    g = g.T[::-1, :]
    move_north(g)
    # pp(g[::-1, :])
    g = g.T[::-1, :]
    move_north(g)
    # pp(g[::-1, :].T[::-1, :])
    return g[::-1, :].T[::-1, :]

prev_states = [grid.copy()]
n_round = 1000000000
last_grid = None
for i in range(1, 10000):
    if last_grid is not None: break
    grid = apply_cycle(grid)
    pp(grid)
    for num_apply, prev_state in enumerate(prev_states):
        if np.array_equal(grid, prev_state):
            print("found", num_apply, i)
            cycle_length = i-num_apply
            last_grid = prev_states[num_apply + (n_round - num_apply)%(cycle_length)]
    prev_states.append(grid.copy())


pp(last_grid)
load = 0
for c_idx in range(len(last_grid[0])):
    for r_idx in range(len(last_grid)):
        if last_grid[r_idx][c_idx] == "O":
            load += len(grid) - r_idx
print(load)
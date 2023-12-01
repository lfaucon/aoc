import math
grid, digits = [list(line) for line in open("3.txt").read().splitlines()], set("0123456789")
gears = [(r_i, c_i) for r_i, r in enumerate(grid) for c_i, c in enumerate(r) if c == "*"]

numbers, num_at_pos = [], {}
current_number, current_number_index = [], 0
for row_index in range(len(grid)):
    for col_index in range(len(grid[row_index])):
        if grid[row_index][col_index] in digits:
            current_number.append((row_index, col_index))
            num_at_pos[(row_index, col_index)] = current_number_index
        if col_index == len(grid[row_index]) - 1 or grid[row_index][col_index] not in digits:
            if current_number:
                numbers.append(int(''.join(grid[r][c] for r,c in current_number)))
                current_number, current_number_index = [], current_number_index + 1

moves = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
get_adj = lambda r, c: set(num_at_pos.get((r+x, c+y)) for x, y in moves).difference({None})
adj_number_indices = [get_adj(*gear) for gear in gears]
print(sum(math.prod(numbers[idx] for idx in adj) for adj in adj_number_indices if len(adj) == 2))

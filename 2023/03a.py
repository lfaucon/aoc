grid = [list(line) for line in open("3.txt").read().splitlines()]

digits = set("0123456789")

numbers_positions = []
current_number_start, current_number_end = None, None
for row_index in range(len(grid)):
    for col_index in range(len(grid[row_index])):
        print(row_index, col_index)
        print(current_number_start, current_number_end)
        if grid[row_index][col_index] in digits:
            if current_number_start is None:
                current_number_start = col_index
            current_number_end = col_index
        if col_index == len(grid[row_index]) - 1 or grid[row_index][col_index] not in digits:
            if current_number_start is not None:
                numbers_positions.append((row_index, current_number_start, current_number_end))
                current_number_start, current_number_end = None, None
print(numbers_positions)
numbers = [int(''.join(grid[r][cs:ce+1])) for r,cs,ce in numbers_positions]
print(numbers)
def is_valid(row_index, col_start, col_end):
    if col_start > 0 and grid[row_index][col_start-1] != '.':
        return True
    if col_end < len(grid[row_index]) - 1 and grid[row_index][col_end+1] != '.':
        return True
    range_to_search = list(range(max(0,col_start-1), min(col_end+2, len(grid[row_index]))))
    if row_index > 0 and any(grid[row_index-1][k] != '.' for k in range_to_search):
        return True
    if row_index < len(grid) -1 and any(grid[row_index+1][k] != '.' for k in range_to_search):
        return True
    return False
print(sum(n for np, n in zip(numbers_positions, numbers) if is_valid(*np)))
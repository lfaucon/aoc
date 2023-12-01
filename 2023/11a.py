space = [list(l) for l in open("11.txt").read().splitlines()]
row_to_double = [row_idx for row_idx, row in enumerate(space) if all(c == "." for c in row)]
print(row_to_double)
col_to_double = [col_idx for col_idx in range(len(space[0])) if all(row[col_idx] == "." for row in space)]
print(col_to_double)
galaxies = [
    (row_idx, col_idx)
    for row_idx in range(len(space))
    for col_idx in range(len(space[0]))
    if space[row_idx][col_idx] == "#"
]
print(galaxies)
def distance(g_1, g_2):
    r_1, c_1 = g_1
    r_2, c_2 = g_2
    r_1, r_2 = min(r_1, r_2), max(r_1, r_2)
    c_1, c_2 = min(c_1, c_2), max(c_1, c_2)
    # print([r_1 < r < r_2 for r in row_to_double])
    # print(r_1, r_2, row_to_double)
    # print(
    #     r_2 - r_1,
    #     sum(r_1 < r < r_2 for r in row_to_double) ,
    #     c_2 - c_1 ,
    #     sum(c_1 < c < c_2 for c in col_to_double),
    # )
    return (
        r_2 - r_1 
        + 999999 * sum(r_1 < r < r_2 for r in row_to_double) 
        + c_2 - c_1 
        + 999999 * sum(c_1 < c < c_2 for c in col_to_double)
    )

print(distance(galaxies[7], galaxies[8]))
print(sum(
    distance(galaxies[g_1], galaxies[g_2])
    for g_1 in range(len(galaxies)-1)
    for g_2 in range(g_1+1, len(galaxies))
))
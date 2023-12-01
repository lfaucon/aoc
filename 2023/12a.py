from itertools import permutations

lines, conditions = zip(*[l.split(" ") for l in open("12.txt").read().splitlines()])
conditions = [tuple(map(int, c.split(","))) for c in conditions]

def get_permutations(m, n):
    if n == 0: return {"#"*m}
    if m == 0: return {"."*n}
    return {
        "#"+perm for perm in get_permutations(m-1, n)
    }.union({
        "."+perm for perm in get_permutations(m, n-1)
    })

def extract_groups(line):
    # print("Extracting groups for", line)
    found_groups = []
    current_group_size = 0
    for c in line:
        if c == "." and current_group_size > 0:
            found_groups.append(current_group_size)
            current_group_size = 0
        if c == "#":
            current_group_size += 1
    if current_group_size > 0:
        found_groups.append(current_group_size)
    # print("Found groups", found_groups)
    return tuple(found_groups)

def count_arrangements(line, condition):
    n_q = len([c for c in line if c == "?"])
    n_h = len([c for c in line if c == "#"])
    n_h_missing = sum(condition) - n_h
    if n_h_missing > n_q: return 0
    count_correct_replacements = 0

    for replacement in get_permutations(n_h_missing, n_q-n_h_missing):
        rep_idx = 0
        new_line = []
        for c in line:
            if c == "?":
                new_line.append(replacement[rep_idx])
                rep_idx += 1
            else:
                new_line.append(c)
        if extract_groups(new_line) == condition:
            count_correct_replacements += 1
    return count_correct_replacements

# test_idx = 475
# line, condition = lines[test_idx], conditions[test_idx]
# count = count_arrangements(line, condition)
# print(">"*64)
# print(line, condition, count)
# print(">"*64)
# exit()

all_arrangements_counts = []
    
for line, condition in zip(lines, conditions):
    print("Counting for line -> ", line, condition)
    count = count_arrangements(line, condition)
    all_arrangements_counts.append(count)
    print("Found count", count)

print(all_arrangements_counts)
print(sum(all_arrangements_counts))

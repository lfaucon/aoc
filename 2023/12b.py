import functools
lines, conditions = zip(*[l.split(" ") for l in open("12.txt").read().splitlines()])
conditions = [tuple(map(int, c.split(","))) for c in conditions]
lines = ["?".join([l,l,l,l,l]) for l in lines]
conditions = [c+c+c+c+c for c in conditions]

def extract_groups(line, include_last=False):
    found_groups, last_group = [], None
    current_group_size = 0
    for c in line:
        if c == "." and current_group_size > 0:
            found_groups.append(current_group_size)
            current_group_size = 0
        if c == "#":
            current_group_size += 1
    if current_group_size > 0:
        last_group = current_group_size
    if include_last:
        return tuple(found_groups + [last_group]) if last_group is not None else tuple(found_groups)
    return tuple(found_groups), last_group

@functools.cache
def count_arrangements(line, condition):
    if len(condition) == 0:
        only_dots = int(all(c in {".", "?"} for c in line))
        return only_dots
    if all(c != "?" for c in line):
        line_is_correct = int(extract_groups(line, include_last=True) == condition)
        return line_is_correct
    first_q_idx = line.index("?")
    found_groups_before_q, last_group_before_q = extract_groups(line[:first_q_idx])
    next_group_idx = len(found_groups_before_q)
    if next_group_idx >= len(condition) + (last_group_before_q is None):
        return 0
    if found_groups_before_q != condition[:next_group_idx]:
        return 0
    if last_group_before_q is not None:
        if last_group_before_q <= condition[next_group_idx]:
            missing_h = condition[next_group_idx] - last_group_before_q
            if all(c in {"?", "#"} for c in line[first_q_idx:first_q_idx+missing_h]) and (first_q_idx+missing_h == len(line) or (first_q_idx+missing_h < len(line) and line[first_q_idx+missing_h] in {".", "?"})):
                count_continuing_current = count_arrangements(
                    line[first_q_idx+missing_h+1:],
                    condition[next_group_idx+1:],
                )
                return count_continuing_current
        return 0
    
    count_not_using_q = count_arrangements(
        line[first_q_idx+1:],
        condition[next_group_idx:],
    )
    
    if next_group_idx < len(condition):
        current_condition = condition[next_group_idx]
        a, b = first_q_idx, first_q_idx+current_condition
        if all(c == "?" or c=="#" for c in line[a:b]) and (b == len(line) or (b < len(line) and line[b] in {".", "?"})):
            count_using_q = count_arrangements(line[b+1:], condition[next_group_idx+1:],)
            return count_using_q+count_not_using_q

    return count_not_using_q

all_arrangements_counts = []
    
for line, condition in zip(lines, conditions):
    print("Counting for line -> ", line, condition)
    count = count_arrangements(line, condition)
    all_arrangements_counts.append(count)
    print("Found count", count)

print(sum(all_arrangements_counts))
assert 2043098029844 == sum(all_arrangements_counts)

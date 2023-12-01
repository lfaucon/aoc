import numpy as np
# AREA_LOW, AREA_HIGH = 7, 27
AREA_LOW, AREA_HIGH = 200000000000000, 400000000000000
parse_numbers = lambda x: list(map(int, x.split(",")))
positions, speeds = zip(*[l.split("@") for l in open("24.txt").read().splitlines()])
positions = np.array([parse_numbers(p) for p in positions])[:, :2]
speeds = np.array([parse_numbers(s) for s in speeds])[:, :2]
# print(positions)
# print(speeds)


def get_intersect(a_idx, b_idx):
    # pa + t * va = pb + k * vb
    try:
        S = np.concatenate([speeds[[a_idx], :], -speeds[[b_idx], :]], axis=0).T
        solved = np.linalg.solve(S,positions[b_idx] - positions[a_idx])
        # print(S)
        # print(speeds[a_idx, :])
        # print(solved)
        # print(positions[a_idx] + speeds[a_idx, :] * solved[0])
        # print(positions[b_idx] + speeds[b_idx, :] * solved[1])
        if solved[0] < 0 or solved[1] < 0:
            return None
        intersection = positions[b_idx] + speeds[b_idx, :] * solved[1]
        return intersection
    except np.linalg.LinAlgError:
        return None
    
# print(get_intersect(0, 4))
# exit()

count = 0
for a_idx in range(len(positions)):
    for b_idx in range(a_idx+1, len(positions)):
        intersection = get_intersect(a_idx, b_idx)
        if intersection is None:
            print("No intersection:", intersection, a_idx, b_idx)
        elif np.all(AREA_LOW <= intersection) and np.all(intersection <= AREA_HIGH):
            print("Intersection within bounds: ", intersection, a_idx, b_idx)
            count += 1
        else:
            print("Intersection outside bounds:", intersection, a_idx, b_idx)
print(count)
import numpy as np
# AREA_LOW, AREA_HIGH = 7, 27
# AREA_LOW, AREA_HIGH = 200000000000000, 400000000000000
parse_numbers = lambda x: list(map(int, x.split(",")))
positions, speeds = zip(*[l.split("@") for l in open("24.txt").read().splitlines()])
positions = np.array([parse_numbers(p) for p in positions])
speeds = np.array([parse_numbers(s) for s in speeds])
# print(positions)
# print(speeds)


def get_intersect(pa, va, pb, vb):
    # pa + t * va = pb + k * vb
    try:
        S = np.concatenate([va, -vb], axis=0).T
        solved = np.linalg.solve(S,pb-pa)
        # if solved[0] < 0 or solved[1] < 0:
        #     return None
        return pb + vb * solved[1]
    except np.linalg.LinAlgError:
        return None

# print(get_intersect(0, 4))
# exit()

# count = 0
# for a_idx in range(len(positions)):
#     for b_idx in range(a_idx+1, len(positions)):
#         intersection = get_intersect(a_idx, b_idx)
#         if intersection is None:
#             print("No intersection:", intersection, a_idx, b_idx)
#         elif np.all(AREA_LOW <= intersection) and np.all(intersection <= AREA_HIGH):
#             print("Intersection within bounds: ", intersection, a_idx, b_idx)
#             count += 1
#         else:
#             print("Intersection outside bounds:", intersection, a_idx, b_idx)
# print(count)

def do_collision(pa, va, pb, vb):
    # pa + t * va = pb + t * vb
    # pa - pb = t * (vb - va)
    if all((pa-pb)[c1] * (vb-va)[c2] == (pa-pb)[c2] * (vb-va)[c1] for c1,c2 in [(0,1), (0,2), (1,2)]):
        return True
    else:
        return False


# for time_hit_first in range(10000):
#     for time_hit_second in range(10000):
#         if time_hit_first == time_hit_second:
#             continue
#         X1 = positions[0] + time_hit_first * speeds[0]
#         X2 = positions[1] + time_hit_second * speeds[1]
#         S = (X2-X1) / (time_hit_second - time_hit_first)
#         X = X1 - S * time_hit_first
#         # print(X1)
#         # print(X2)
#         # print(X, S)
#         if all(do_collision(X, S, positions[idx], speeds[idx]) for idx in range(len(positions))):
#             print("Found:", X, S, time_hit_first, time_hit_second)
#             exit()
# print("Did not find anything . . .")

from sympy import *

X1, X2, X3 = positions[0], positions[1], positions[2]
S1, S2, S3 = speeds[0], speeds[1], speeds[2]

t1, t2, t3 = symbols('t1 t2 t3')
solution = solve([
    Eq((t2 - t3) * (X1[c] + t1 * S1[c]) + (t3 - t1) * (X2[c] + t2 * S2[c]) + (t1 - t2) * (X3[c] + t3 * S3[c]), 0)
    for c in [0,1,2]
], [t1, t2, t3])

print(solution)
_t1, _t2, _t3 = solution[1]

S = (X2 + _t2 * S2 - X1 - _t1 * S1) / (_t2 - _t1)
X = X1 + _t1 * (S1 - S)
print(sum(X))

# > {n: 108.767303889255, Y1: 0.545154911008569, Y2: 0.454845088991430}

# S = (X2 + t2 * S2 - X1 - t1 * S1) / (t2 - t1)
# X = X1 + t1 * (S1 - S)

# X + t3 * S = X3 + t3 * S3

# X1 + t1 * (S1 - S) + t3 * S = X3 + t3 * S3
# X1 + t1 * S1 + (t3 - t1) * S = X3 + t3 * S3
# X1 + t1 * S1 + (t3 - t1) * (X2 + t2 * S2 - X1 - t1 * S1) / (t2 - t1) = X3 + t3 * S3

#  (t2 - t1) * (X1 + t1 * S1) + (t3 - t1) * (X2 + t2 * S2 - X1 - t1 * S1) =  (t2 - t1) * (X3 + t3 * S3)

#  (t2 - t3) * (X1 + t1 * S1) + (t3 - t1) * (X2 + t2 * S2) + (t1 - t2) * (X3 + t3 * S3) = 0

#  (X3 - X2) * t1 + (X2 - X1) * t3 + (X1 - X3) * t2 + 
import numpy as np
patterns = [pattern for pattern in open("13.txt").read().split("\n\n")]
patterns = [np.array([[int(c == "#") for c in line] for line in pattern.splitlines()]) for pattern in patterns]
print(patterns)

def find_mirror(pattern):
    for k in range(1, pattern.shape[0]):
        length = min(k, pattern.shape[0]-k)
        if np.abs(pattern[(k-length):k, :] - pattern[(k+length-1):k-1:-1, :]).sum() == 1:
            return k
    return 0

mirror_positions = [
    100* find_mirror(pattern) + find_mirror(pattern.T)
    for pattern in patterns
]
print(mirror_positions)
print(sum(mirror_positions))
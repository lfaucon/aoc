import numpy as np
patterns = [pattern for pattern in open("13.txt").read().split("\n\n")]
patterns = [np.array([[int(c == "#") for c in line] for line in pattern.splitlines()]) for pattern in patterns]
print(patterns)

def find_mirror(pattern):
    for k in range(1, pattern.shape[0]):
        length = min(k, pattern.shape[0]-k)
        if np.array_equal(
            pattern[(k-length):k, :],
            pattern[(k+length-1):k-1:-1, :]
        ):
            return k
    return 0

print(find_mirror(patterns[5]))

mirror_positions = [
    100* find_mirror(pattern) + find_mirror(pattern.T)
    for pattern in patterns
]
print(mirror_positions)
print(sum(mirror_positions))
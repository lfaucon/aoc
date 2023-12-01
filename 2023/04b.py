lines = [l.split(":")[1].split("|") for l in open("4.txt").read().splitlines()]
extract_numbers = lambda x: set(map(int, [a for a in x.strip().split(" ") if a]))
matches = [len(extract_numbers(winning) & extract_numbers(card)) for winning, card in lines]
counts = [1 for _ in matches]
for idx, p in enumerate(matches):
    for k in range(idx+1, min(len(counts), idx+p+1)):
        counts[k] += counts[idx]
print(sum(counts))
lines = [l.split(":")[1].split("|") for l in open("4.txt").read().splitlines()]
extract_numbers = lambda x: set(map(int, [a for a in x.strip().split(" ") if a]))
matches = [len(extract_numbers(winning) & extract_numbers(card)) for winning, card in lines]
print(sum(2 ** (m-1) if m > 0 else 0 for m in matches))
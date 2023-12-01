hash = lambda word: ((hash(word[:-1]) + ord(word[-1]))*17)%256 if word else 0
print(sum(map(hash, open("15.txt").read().strip().split(","))))

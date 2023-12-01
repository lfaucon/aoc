instructions = open("15.txt").read().strip().split(",")
hash = lambda word: ((hash(word[:-1]) + ord(word[-1]))*17)%256 if word else 0

boxes = [{} for _ in range(256)]
for instruction in instructions:
    if instruction[-1] == "-":
        key = instruction[:-1]
        if key in boxes[hash(key)]:
            del boxes[hash(key)][key]
    else:
        key, value = instruction.split("=")
        boxes[hash(key)][key] = int(value)

total = 0
for box_idx, box in enumerate(boxes):
    for key_idx, key in enumerate(box):
        total += (box_idx+1) * (key_idx + 1) * box[key]

print(total)
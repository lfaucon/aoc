instructions, connections = open("8.txt").read().split("\n\n")
connections = {
    line[:3]: {'L': line[7:10], 'R': line[12:15]}
    for line in connections.splitlines()
}
instruction_idx, position = 0, 'AAA'
while position != 'ZZZ':
    position = connections[position][instructions[instruction_idx%len(instructions)]]
    instruction_idx += 1
print(instruction_idx)
histories = [list(map(int,line.split(" "))) for line in open("9.txt").read().splitlines()]
differences = lambda h: [h[i+1] - h[i] for i in range(len(h)-1)]
all_differences = lambda h: [h] if all(x == 0 for x in h) else [h, *all_differences(differences(h))]
complete_history = lambda history_list: sum(h[-1] for h in history_list)
print(sum([complete_history(all_differences(h)) for h in histories]))

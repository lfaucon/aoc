card_values = {card: c_idx for c_idx, card in enumerate("23456789TJQKA")}
hands, bids = zip(*[l.split(" ") for l in open("7.txt").read().splitlines()])
def hand_type(hand):
    counts = {}
    for card in hand: counts[card] = counts.get(card, 0) + 1
    count_value = tuple(sorted(counts.values(), reverse=True))
    card_value = tuple(card_values[c] for c in hand)
    return count_value + card_value
hand_types = [hand_type(h) for h in hands]
_, sorted_bids = zip(*sorted([(h, b) for b, h in zip(bids, hand_types)]))
print(sum([int(bid) * (b_idx+1) for b_idx, bid in enumerate(sorted_bids)]))

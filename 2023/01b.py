subs = "one,o1e,two,t2o,three,t3e,four,4,five,5e,six,6,seven,7n,eight,e8t,nine,n9e".split(",")
rewrite_digits = lambda l, subs: rewrite_digits(l.replace(*subs[:2]), subs[2:]) if subs else l
rewritten_lines = [rewrite_digits(l, subs) for l in open("day_1_input.txt").read().splitlines()]
digits_in_line = [[c for c in line if c in "0123456789"] for line in rewritten_lines]
print(sum(int(digit_list[0] + digit_list[-1]) for digit_list in digits_in_line))

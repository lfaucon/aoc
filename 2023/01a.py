lines = open("1.txt").read().splitlines()
digits_in_line = [[c for c in line if c in "0123456789"] for line in lines]
print(sum(int(digit_list[0] + digit_list[-1]) for digit_list in digits_in_line))

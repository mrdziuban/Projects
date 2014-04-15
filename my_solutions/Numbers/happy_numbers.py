def is_happy_number(n):
	seen_nums = []
	while True:
		res = sum(int(d) ** 2 for d in str(n))
		if res == 1:
			return True
		elif res in seen_nums:
			return False
		else:
			n = res
			seen_nums.append(n)

happy_nums = []
n = int(input('Start at: '))

while len(happy_nums) < 8:
	if is_happy_number(n):
		happy_nums.append(n)
		print(len(happy_nums))
	n += 1

print(happy_nums)
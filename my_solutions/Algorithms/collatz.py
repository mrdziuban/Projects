def record_collatz(n):
	steps = 0
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = n * 3 + 1
		steps += 1
	return steps

n = int(input('Enter a number greater than 1: '))
if n < 1:
	print("That wasn't greater than 1.")
else:
	print('It took ' + str(record_collatz(n)) + ' steps to reach 1')
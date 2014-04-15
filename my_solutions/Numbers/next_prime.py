def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def find_next(n):
	n += 1
	while not is_prime(n):
		n += 1
	return n

def loop(start):
	user_input = input('Find next prime? (y/n): ')
	if user_input == 'n':
		return
	prime = find_next(start)
	print(prime)
	loop(prime)

loop(0)
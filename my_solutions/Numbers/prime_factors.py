def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

n = int(input('Enter num: '))
res = []

for i in range(2, n+1):
	while n % i == 0:
		if is_prime(i):
			res.append(i)
			n /= i

print(res)
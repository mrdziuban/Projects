def fact_iter(n):
	if n == 0:
		return 1
	res = 1
	while n > 1:
		res *= n
		n -= 1
	return res

def fact_recurs(n):
	if n == 0 or n == 1:
		return 1
	return n * fact_recurs(n - 1)

n = int(input('Enter a number: '))
print('The factorial of ' + str(n) + ' is ' + str(fact_recurs(n)))
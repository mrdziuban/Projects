def primes_to(n, start = 2):
	if start >= n:
		return
	nums = range(2, n + 1)
	marked_nums = []
	done = [2]
	try:
		while start <= n:
			print(start)
			marked_nums += [start * i for i in range(start, n) if start * i <= n]
			diff = [x for x in nums if x not in marked_nums]
			start = next(x for x in sorted(diff) if x != start and x not in done)
			done.append(start)
	except StopIteration:
		pass

n = int(input('Enter the ending number: '))
primes_to(n)
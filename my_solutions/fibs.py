n = int(raw_input('Enter a number of fibs: '))
arr = [0,1]

if n < 0:
	print 'Must be a positive number'
elif n <= 2:
	print arr[0:n]
else:
	while len(arr) < n:
		arr.append(arr[-1] + arr[-2])
	print arr
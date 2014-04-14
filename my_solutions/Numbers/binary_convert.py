def dec_to_bin():
	num = int(raw_input('Enter a decimal number: '))
	if num == 0:
		return '0'
	res = ''
	while num:
		if num & 1 == 1:
			res = '1' + res
		else:
			res = '0' + res
		num >>= 1
	return res

def bin_to_dec():
	num = raw_input('Enter a binary number: ')
	num = num[::-1]
	i = 1
	res = 0
	for l in num:
		res += (i * int(l))
		i *= 2
	return res

print '1. Decimal to binary\n2. Binary to decimal'
selection = int(raw_input('Enter your selection: '))
if selection == 1:
	print dec_to_bin()
elif selection == 2:
	print bin_to_dec()
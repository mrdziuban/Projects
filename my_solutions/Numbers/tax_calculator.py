def calculate_tax(amt, tax):
	return amt * (1.0 + tax)

amt = float(input('Enter a dollar amount: $'))
tax = float(input('Enter the tax amount (decimal): '))
print('Your total is $' + str(calculate_tax(amt, tax)))
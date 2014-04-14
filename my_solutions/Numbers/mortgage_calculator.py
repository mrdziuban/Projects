def calculate(m, i, y):
	original_mortgage = m
	for year in range (0, y):
		print m
		amt = (m/(y - year))/12.0
		print 'Year '+str(year + 1)+': $%.2f per month' % amt
		m -= (amt * 12)
		m += (original_mortgage * i)
		original_mortgage *= (1.0 + i)

total_mortgage = int(raw_input('Enter the amount of your mortgage: $'))
interest = float(raw_input('Enter your interest rate (decimal): '))
years = int(raw_input('Enter number of years of payment: '))
calculate(total_mortgage, interest, years)
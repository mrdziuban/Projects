def make_change(amt):
	amt *= 100
	coins = [25, 10, 5, 1]
	for coin in coins:
		func_name = 'coin_'+str(coin)
		coin_name = globals()[func_name]()
		num_coins = int(amt) // int(coin)
		print(str(num_coins) + ' ' + coin_name)
		amt -= (num_coins * coin)

def coin_25():
	return 'quarters'
def coin_10():
	return 'dimes'
def coin_5():
	return 'nickels'
def coin_1():
	return 'pennies'

amt = float(input('Enter an amount: $'))
make_change(amt)
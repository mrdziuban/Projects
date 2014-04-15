from random import randint

def flip_coin():
	return 'Heads' if randint(0, 1000) < 500 else 'Tails'

def loop():
	flip_counts = {'Heads': 0, 'Tails': 0}
	play = 'y'
	while play != 'n':
		play = input('Flip coin? (y/n) ')
		if play == 'y':
			flip = flip_coin()
			print(flip)
			flip_counts[flip] += 1
	print(flip_counts)

loop()
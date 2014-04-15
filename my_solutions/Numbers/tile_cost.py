def calculate_cost(cost, dims):
	dims = dims.split('x')
	width = int(dims[0].strip())
	height = int(dims[1].strip())
	return width * height * cost

cost = float(input('Enter a cost per tile. $'))
dims = input('Enter the dimensions of the floor: (e.g. 10x10) ')
print('$%.2f' % calculate_cost(cost, dims))
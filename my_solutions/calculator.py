import re

def handle_nums(num1, op, num2):
	if op == '+':
		return num1 + num2
	elif op == '-':
		return num1 - num2
	elif op == 'x' or op == '*':
		return num1 * num2
	elif op == '/':
		return num1 / num2
	else:
		return 0

def calculate(exp):
	parts = re.split('(\-?\d+\.?\d*)', expression)
	parts = parts[1:-1]
	while len(parts) > 1:
		res = handle_nums(int(str(parts[0]).strip()), parts[1].strip(), int(parts[2].strip()))
		parts[0] = res
		del parts[1]
		del parts[1]
	return parts[0]

expression = raw_input('Enter your expression: ')
print expression + ' = ' + str(calculate(expression))
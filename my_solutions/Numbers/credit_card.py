def check_cc(cc):
	cc = cc.replace(' ', '')
	doubled_cc_nums = []
	other_nums = []
	for i, l in enumerate(cc):
		doubled_cc_nums.append(int(l) * 2) if i % 2 == 0 else other_nums.append(int(l))
	total = 0
	for i in range(0, len(other_nums)):
		if doubled_cc_nums[i] < 10:
			total += doubled_cc_nums[i]
		if other_nums[i] < 10:
			total += other_nums[i]
		if doubled_cc_nums[i] >= 10:
			total += (int(str(doubled_cc_nums[i])[0]) + int(str(doubled_cc_nums[i])[1]))
		if other_nums[i] >= 10:
			total += (int(str(other_nums[i])[0]) + int(str(other_nums[i])[1]))
	return total % 10 == 0

cc_num = input('Enter a CC number: ')
print(check_cc(cc_num))
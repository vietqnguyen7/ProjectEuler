def mod(x): return x%2

if __name__ == '__main__':
	number_list = range(1,20)
	check = False
	num = 1
	while check == False:
		num += 1
		new_num = list(filter(lambda x: num%x, number_list))
		if len(new_num) == 0:
			check = True
		print(new_num)
	print(num)
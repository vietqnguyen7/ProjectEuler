if __name__ == '__main__':
	num = int(input("Input a number to find the sum of all the multiples of 3 or 5 under that number\n"))
	sum = 0
	x = 0
	while x < num:
		if x%3 == 0 or x%5 == 0:
			sum += x
		x+=1
	print("The sum of all the multiples of 3 and 5 under " + str(num) + " is " + str(sum))
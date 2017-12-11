if __name__ == '__main__':
	num = int(input("Find the sum of the even-values terms in the fibonacci sequence that does not exceed what number:\n"))
	t1 = 1
	t2 = 2
	sum = 0
	while t1 < num:
		if t1%2 == 0:
			sum += t1
		nextTerm = t1 + t2
		t1 = t2
		t2 = nextTerm
	print("The sum of the even fibonacci sequence values terms under " + str(num) + " is " + str(sum))
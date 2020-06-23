def find(ravi, salma):

	count = 0
	for i, num in enumerate(salma):
		if i == ravi.index(num):
			ravi.remove(num)
			salma.remove(num)
			count += 1
		else:
			index = ravi.index(num)
			ravi.rotate(index)
			count += 1
			if i == ravi.index(num):
				ravi.remove(num)
				salma.remove(num)
				count += 1
	return count

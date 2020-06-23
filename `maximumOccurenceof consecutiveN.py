#Given a sorted array A of size n, find an element that occurs more than n/2 times?
# 1,1,1,1,2,3,3,4
def Solution(array):
	numValues = len(array) // 2
	for i in range(len(array)):
		firstElement = array[i]
		lastElement = array[numValues]
		if firstElement == lastElement:
			requiredNumber =  array[i]
			break
		else:
			continue
	return requiredNumber
print(Solution([1,1,1,1,2,3,3,4]))

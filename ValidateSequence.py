#Problem Name:Validate SubSequence
#This question is from algoexpert



def isValidSubsequence(array, sequence):
	d = dict()
	n = []
	for i, num in enumerate(array):
		if num in sequence:
			d[num] = i
	for i in d.values():
		if not n:
			n.append(i)
		else:
			if n[-1] < i:
				n.append(i)
			else:
				return False
	return True

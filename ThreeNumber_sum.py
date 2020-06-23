#Problem Name: Three number Sum
#Descrition : Given an array, from the array find the elements from the array that sums
# to the given target.

#problem by Algoexpert
#sample Input: ([12,3,1,2,-6,5,-8,6], 0)
# where the given array = [12,3,1,2,-6,5,-8,6] and target = 0
#Output must be: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# Solution:
def Solution(array, target):
	array.sort()
	triplet = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == target:
				triplet.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < target:
				left += 1
			elif currentSum > target:
				right -= 1
	return triplet
#this is the Solution Given by AlgoExpert.

# max_left = represents the indices from left upto
# max_right = represents the indices left to  right
# left_sum + right_sum = maximum sum generated from the left_sum to right_sum indices



def Solution(array, low, mid, high):
	left_sum = -1
	s = 0
	for i in range(mid, low, -1):
		s = s + array[i]
		if s > left_sum:
			left_sum = s
			max_left = i
	right_sum = -1
	s = 0
	for j in range(mid + 1, high):
		s = s + array[j]
		if s > right_sum:
			right_sum = s
			max_right = j
	return (max_left, max_right, left_sum + right_sum)
array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
mid = (0 + len(array)) // 2
print(Solution(array, 0, mid, len(array)))

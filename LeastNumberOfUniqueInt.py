
#findLeastNumOfUniqueInts from leetcode
def findLeastNumOfUniqueInts(arr, k):

	cnt = collections.Counter(arr)
	print(cnt)
	print()
	print(sorted( cnt.values() ) )
	for ans, times in enumerate( sorted( cnt.values() ) ):

		k -= times
		if k < 0:
			return len(cnt) - ans
	return 0

#This is the code for consecutive Characters in string
#for example: s = "leetcode"
#the ans is 2 because e has the maximum consecutive length

def Solution(s):
	res = 1
	l = 1
	for i in range(1, len(s)):
		if a[i -1] == a[i]:
			l += 1
			res = max(res, l)
		else:
			l = 1
	return res

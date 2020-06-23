#Is Subsequence Problem From leetcode June
def isSubsequence(s, target):
    iter_target = iter(target)
    return all(char in iter_target for char in s)
s = "abc"
target = "ahbgdc"
print(isSubsequence(s, target))

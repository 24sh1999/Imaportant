##Problem Name : Leetcode Week 2 problem
## Problem  Name: Valid Perfect Square
##Time 32 ms
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        the_sum = 0
        while the_sum < num: 
            the_sum += i 
            if the_sum == num: 
                return True
            i += 2
        return False







##Time 16 MS
##class Solution:
##    def isPerfectSquare(self, num: int) -> bool:
##        l = 1
##        r = num
##        while(r >= l):
##            mid = int((l + r) / 2)
##            if mid ** 2 == num:
##                return True
##            elif mid ** 2 > num:
##                r = mid - 1
##            else:
##                l = mid + 1
##        return False

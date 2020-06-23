#problem from leetcode
#Problem Name:"Sort Characters By Frequency"


#This was mine solution

from collections import Counter
from itertools import repeat, chain
class Solution:
    def frequencySort(self, s: str) -> str:
        num =  list(chain.from_iterable(repeat(i, c) for i,c in Counter(s).most_common()))
        return "".join(num)






#This was the solution submitted by some one else with time of 20ms

#import collections 
#import heapq

#class Solution:
#   def frequencySort(self, s: str) -> str:
#        counterMap = collections.Counter(s)
#        res = ''
#        hq = []
#        for char, freq in counterMap.items():
#            heapq.heappush(hq, (-freq, char))
#
#       while hq:
#            freq, char = heapq.heappop(hq)
#            res += -freq*char
#            
#        return res


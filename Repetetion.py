#Repetetion Character
from itertools import groupby
from operator import itemgetter
def Solution(string):
    groups = groupby(string)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    r = max(result,key=itemgetter(1))[1]
    return r
String = input()
print(Solution(String))

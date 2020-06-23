

#Sorting the elemets based on their frequency
from collections import defaultdict
import collections
import operator
def Solution(String):
    countString = defaultdict(lambda: 0)
    for x in String:
        countString[x] += 1
    
    countString = sorted(countString.items(), key = operator.itemgetter(1)) # it sort the item based on the value
    sorted_dict = collections.OrderedDict(countString)
    
    a = max(sorted_dict.values())
    return a
String = input()
print(Solution(String))

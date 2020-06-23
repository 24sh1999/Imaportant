## Problem from Leetcode Rearrange Words in a Sentence

# 1st Solution

#class Solution:
#    def arrangeWords(self, text: str) -> str:
#        words = text.split(' ')
#        words[0] = words[0].lower()
#        words.sort(key=len)
#        words[0] = words[0].capitalize()
#        return ' '.join(words)


# 2nd Solution

#from functools import cmp_to_key

#class Solution:
#    def arrangeWords(self, text: str) -> str:
#        def arrangeSort(t1, t2):
#            if len(t1) > len(t2):
#                return 1 
#            elif len(t1) < len(t2):
#                return -1
#            else:
#                return 1
#        text = text[0].lower() + text[1:]
#        text = text.split(' ')
#       # list.sort(text, key = cmp_to_key(arrangeSort), reverse=False)
#        list.sort(text, key=len, reverse=False)
#        text[0] = text[0][0].upper() + text[0][1:]
        
 #       return ' '.join(text)

#3rd
#class Solution:
#    def arrangeWords(self, text: str) -> str:
#        return " ".join(sorted(text.split(" "), key=len)).capitalize()

#4th
#class Solution:
#    def arrangeWords(self, text: str) -> str:
#        d = collections.defaultdict(list)
#        for word in text.split(' '):
#            d[len(word)].append(word.lower())
#        res = []
#        for l in sorted(d.keys()):
 #           res += d[l]
#        res = " ".join(res)
#        return res[0].upper() + res[1:]

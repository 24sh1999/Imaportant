#LinearSearch Using Recurssion

def LinearSearch(array, val):
    def linear(array, i, val):
        
        if i < len(array):
            
            if array[i] == val:
                return i
            else:
                i += 1
                res = linear(array, i, val)
                return res
        return -1
    res = linear(array, 0, val)
    
    return res
n = int(input())
array = list(map(int, input().split()))
val = int(input("enter the val you want to search"))

print(LinearSearch(array,val))
        

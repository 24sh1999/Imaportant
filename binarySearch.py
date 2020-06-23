#Binary Search
def Solution(array, val):
    i = 0
    j = len(array) - 1
    while i <= j:
        mid = (i + j)  // 2
        if array[mid] == val:
            return mid
        elif array[mid] > val:
            j = mid - 1
        elif array[mid] < val:
            i = mid + 1
    return -1

                   
n = int(input("Enter the lenght of array:"))
array = list(map(int, input().split()))

val = int(input("Enter the value you want to search:"))
print(Solution(array,val))

#Bubble Sort
def Solution(array):
    i = 0
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j + 1], array[j]
    return array
n = int(input())
array = list(map(int, input().split()))
print(Solution(array))

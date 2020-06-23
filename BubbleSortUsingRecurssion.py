# BubbleSort Using Recurssion
def solution(array):
    def BubbleSort(i, j, array):
        if len(array) == 1:
            return array
        if array[j] > array[j + 1]:
            array[j], array[j+1] = array[j+1], array[j]
        if j < len(array) - 2:
            j += 1
            BubbleSort(i, j, array)
        else:
            if i < len(array):
                i += 1
                j = 0
                BubbleSort(i, j, array)
        return array
    res = BubbleSort(0, 0, array)
    return res

n = int(input())
array = list(map(int, input().split()))
print(solution(array))

    

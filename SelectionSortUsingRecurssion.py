# Selection Sort Using Recurssion
def solution(array):
    def SelectionSort(i, j, small, array):
        if j < len(array):
            if array[j] < array[small]:
                small = j
        j += 1
        SelectionSort(i, j, small, array)
        if small != i:
            tmp = array[i]
            array[i] = array[small]
            array[small] = tmp
            
        if i < len(array):
            i += 1
            small = i
            j = i + 1
            res = SelectionSort(i, j, small, array)
        return res
        
    
    res = SelectionSort(0, 1, 0, array)
    print(res)
    
n = int(input())
array = list(map(int, input().split()))
solution(array)

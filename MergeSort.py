def merge_sort(array, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        middleIdx = (leftIdx + rightIdx) // 2
        merge_sort(array, leftIdx, middleIdx)
        merge_sort(array, middleIdx + 1, rightIdx)
        return merge(array, leftIdx, middleIdx, rightIdx)
    return array

def merge(array, leftIdx, middleIdx, rightIdx):
    i, j, k = leftIdx, middleIdx + 1, leftIdx
    SortedArray = [None] * len(array)
    while i <= middleIdx and j <= rightIdx:
        if array[i] <= array[j]:
            SortedArray[k] = array[i]
            i += 1
        else:
            SortedArray[k] = array[j]
            j += 1
        k += 1
    while i <= middleIdx:
        SortedArray[k] = array[i]
        i += 1
        k += 1
    while j <= rightIdx:
        SortedArray[k] = array[j]
        j += 1
        k += 1
    while leftIdx <= rightIdx:
        array[leftIdx] = SortedArray[leftIdx]
        leftIdx += 1
    return array

    
array = [8, 5, 2, 9, 5, 6, 3]
res = merge_sort(array, 0, len(array) - 1)
print(res)
        

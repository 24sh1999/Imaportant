def solution(array, val):
    def BinarySearch(left, right, mid, val, array):
        if left < right:
            mid = (left  + right) // 2
            if array[mid] ==  val:
                return mid
            elif array[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
            res = BinarySearch(left, right, mid, val, array)
            return (array[res], res)

    res = BinarySearch(0, len(array) - 1, 0, val, array)
    return res

print(solution([1,2,5,10,12], 10))

        
        
        

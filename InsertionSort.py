def Solution(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
    return arr



print(Solution([12, 34, 9, 100, 1, 100, 14, 1, 0, 78]))

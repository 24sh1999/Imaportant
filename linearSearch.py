def Solution(array, val):
    for i in array:
        if i == val:
            return array.index(i)
        else:
            continue
    return -1
val = int(input())
print(Solution([1, 2, 3, 4, 4, 5, 6], val))

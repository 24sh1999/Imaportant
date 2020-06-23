#Selection Sort
def Solution(array):
    for i in range(len(array)):
        small = i
        for j in range(i + 1, len(array)):
            if array[j] < array[small]:
                small = j
        if small != i:
            tmp = array[i]
            array[i] = array[small]
            array[small] = tmp
    return array
n = int(input())
array = list(map(int, input().split()))
print(Solution(array))

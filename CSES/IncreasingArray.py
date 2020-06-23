def Solution(array):
    current = array[0]
    for i in range(1, len(array) - 1):
        if current <= array[i]:
            current = array[i]
        else:
            array[i] = current
            

    return current
n = int(input())
array = list(map(int, input().split()))
print(Solution(array))


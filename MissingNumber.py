#Find the Missing Number
def Solution(n, array):
    sumTotal = (n * (n + 1)) / 2
    Sum = 0
    for i in array:
        Sum += i
    return int(sumTotal - Sum)
n = int(input())
num  = list(map(int, input().split()))
print(Solution(n, num))
    
    

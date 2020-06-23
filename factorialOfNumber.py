#factorial of a Number
def Solution(N):
    stack = {}
    for i in range(1, N + 1):
        if i < 2:
            fact = 1
        else:
            fact = i * stack[i - 1]
        stack[i] = fact
    return stack[N]
N = int(input())
print(Solution(N))

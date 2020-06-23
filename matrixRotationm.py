def sumof(n):
    global arr
    if n == 0:
        return False
    i = n
    sum = 0
    if i in arr:
        return i % arr[i] == 0
    while n>0:
        temp = n%10
        n //= 10
        sum += temp
    #print(arr[i])
    arr[i] = sum
    
    return i % sum == 0

arr = {}
n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
flag = False
for i in range(n-1):
    for j in range(n-1):
        if sumof(a[i][j]) and sumof(a[i][j+1]) and sumof(a[i+1][j]) and sumof(a[i+1][j+1]):
            print(a[i][j],a[i][j+1])
            print(a[i+1][j],a[i+1][j+1])
            flag = True
print("-1" if flag is False else "")
            

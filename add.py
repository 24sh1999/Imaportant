def reverse(data,k):
    result = data[0:k]
    c = result[::-1]
    result1 = data[k:len(data)]
    d = result1[::-1]
    for i in d:
        c.append(i)
    print(*c[::])
    
t = int(input())
for i in range(t):
    n,k = input().split()
    arr = list(map(int,input().split()))
    reverse(arr,int(k))
    

"""
def reverse(arr,N,D):
    reverse_list = []
    for i in range(0,len(arr),D):
        reverse_list.extend(arr[i:i+D][::-1])
    return reverse_list
for _ in range(int(input())):
    N,D = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    reversed_list = reverse(arr,N,D)
    print(*reversed_list)
    """

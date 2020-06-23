def Tapping_water(arr,len_):
    count = 0
    for i in range(1,len_ - 1):
        s = min(max(arr[:i]),max(arr[i+1:]))
        count = count + max(s - arr[i],0)
    print(count)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    len_ = len(arr)
    Tapping_water(arr,len_)

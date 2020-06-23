def isprime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
def find_comb(list1):
    comb=[]
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i==j:
                continue
            else:
                comb.append(int(str(list1[i])+str(list1[j])))
    return comb
def fib1(n,a,b):
    fib=[0]*(n+1)
    fib[0]=a
    fib[1]=b
    fib[2]=a+b
    for i in range(3,n+1):
        fib[i]=fib[i-1]+fib[i-2]
        return fib[n-1]
    a,b=map(int,input().split())
    prime_list=[]
    for i in range(a,b+1):
        if isprime(i):
            prime_list.append(i)
prime_list = []
combination=set(find_comb(prime_list))
combination1=[i for i in combination if isprime(i)]
max1=max(combination1)
min1=min(combination1)
ans1=fib1(len(combination1),min1,max1)
print(ans1)

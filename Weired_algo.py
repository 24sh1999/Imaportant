def number(n):
    array = []
    while n != 1:
        if  n % 2 == 0:
            n = n // 2
            array.append(n)
        else:
            n = n * 3 + 1
            array.append(n)
    return array

n = int(input())
c = number(n)
print(n," ".join(map(str, c)))

##r = " ".join(str(c))
##print("{} {}".format(n,r))
    
    

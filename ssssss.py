l=[]
def convert(b):
    if(b==0):
        return l
    dig=b%2
    l.append(dig)
    convert(b//2)

convert(6)
print(l)
l.reverse()
for i in l:
    print(i,end="")

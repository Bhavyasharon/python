c=int(input("enter a integer:"))
a,b=0,1
print(a,",",b,end=",")
for i in range(2,c):
    c=a+b
    a=b
    b=c
    print(c,",",end="")

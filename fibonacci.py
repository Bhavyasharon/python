c=int(input("enter a number:"))
a,b=0,1
print(a,b)
for i in range(1,c):
    c=a+b
    a=b
    b=c
print(c,",",end="")





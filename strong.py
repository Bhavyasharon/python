import math
num=int(input("enter a number:"))
fact=1
sum=0
copy=num
if(num==0):
    sum=sum+fact
else:
    while(copy!=0):
        rem=copy%10
        fact=math.factorial(rem)
        sum=sum+fact
        copy=copy//10
if(sum==num):
    print("strong number")
else:
    print("not strong number")


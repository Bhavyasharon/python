num=int(input("enter a integer: "))
fact=1
if(num==0):
    print("invalid input")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial is ",fact)



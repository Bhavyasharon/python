c=int(input("enter a number:"))
rev=0
while(c>0):
    rem=c%10
    rev=(rev*10)+rem
    c=c//10
print(rev)

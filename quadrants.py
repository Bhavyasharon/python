x= int(input("enter a number: "))
y=int(input("enter a number: "))
if(x>0 and y>0):
    print("This point lies in 1st quadrant")
elif(x<0 and y>0):
    print("This point lies in 2nd quadrant")
elif(x<0 and y<0):
    print("This point lies in 3rd quadrant")
elif(x>0 and y<0):
    print("This point lies in 4th quadrant")
else:
    print("This point lies in origin")

c=int(input("enter a number: "))
if(c>0):
   print("positive")
elif(c<0):
   print("negative")
else:
   print("neither positive nor negative")
# method 2
#print("positive"if c>0 else("negative"if c<0 else("neither negative nor positive")))
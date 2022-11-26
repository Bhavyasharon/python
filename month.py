month=int(input("enter a month: "))
year=int(input("enter a year: "))
if(((month==2) and (year%400==0) or (year%100!=0) and (year%4==0))):
    print(29)
elif(month==2):
    print(28)
elif(month==4 or month==6 or month==9 or month==11):
    print(30)
else:
    print(31)
def getsum(num):
    if num == 1:
        return 1
    return num+getsum(num-1)
num=10
print(getsum(num))

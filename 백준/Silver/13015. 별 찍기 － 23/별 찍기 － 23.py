import math
x = int(input())
xandx = "*"+" "*(x-2)+"*"
for i in range(1, x):
    space = 2*x-2*i-1
    if i == 1:
        print("*"*x+" "*space+"*"*x)
    else:
        print(" "*(i-1)+xandx+" "*space+xandx)
print(" "*(x-1)+xandx+" "*(x-2)+"*")
for i in range(x-1, 0, -1):
    space = 2*x-2*i-1
    if i == 1:
        print("*"*x+" "*space+"*"*x)
    else:
        print(" "*(i-1)+xandx+" "*space+xandx)
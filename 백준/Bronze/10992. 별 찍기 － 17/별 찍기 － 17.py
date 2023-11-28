x = int(input())
for i in range (1, x+1):
    if i == 1:
        print(" "*(x-1)+"*")
    elif i == x:
        print("*"*(2*i-1))
    else:
        space = 1+2*(i-2)
        print(" "*(x-i)+"*"+" "*space+"*")
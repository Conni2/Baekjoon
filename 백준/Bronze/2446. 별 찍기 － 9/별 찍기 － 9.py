x = int(input())
for i in range (x, 0, -1):
    print(" "*(x-i)+"*"*(2*i-1))
for i in range (2, x+1):
    print(" "*(x-i)+"*"*(2*i-1))

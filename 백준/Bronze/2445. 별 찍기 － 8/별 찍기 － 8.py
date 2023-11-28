x = int(input())
for i in range (1, x+1):
    print("*"*i+" "*(2*(x-i))+"*"*i)
for i in range (x-1, 0, -1):
    print("*"*i+" "*(2*(x-i))+"*"*i)
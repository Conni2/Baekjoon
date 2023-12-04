import sys
n = int(sys.stdin.readline())
num =[]
for i in range(n):
    m = int(sys.stdin.readline())
    num.append(m)
num.sort()
for x in range(n):
    print(num[x])
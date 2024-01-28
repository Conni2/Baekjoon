import sys
case = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
x = 0
line.sort()
for i in range(case):
    x += line[i]*(case-i)
print(x)
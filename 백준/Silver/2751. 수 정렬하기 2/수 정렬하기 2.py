import sys
n = int(input())
num = []
for x in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
for i in num:
    print(i)
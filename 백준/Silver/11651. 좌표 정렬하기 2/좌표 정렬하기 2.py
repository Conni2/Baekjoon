import sys
n=int(sys.stdin.readline())
li=[]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li.append([b, a])
li.sort()
for i in li:
    print(i[1], i[0])
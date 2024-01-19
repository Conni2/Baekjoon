import sys
n, l = map(int, sys.stdin.readline().split())
fruits = list(map(int, sys.stdin.readline().split()))
fruits.sort()
for i in range(n):
    if fruits[i] <= l:
        l += 1
    else:
        break

print(l)
import sys
n = int(sys.stdin.readline())
li = [0] * n
for i in range(n):
	li[i] = int(sys.stdin.readline())
li.reverse()
x, temp = 0, li[0]
for k in range(1, n):
	if temp <= li[k]:
		temp -= 1
		x += li[k] - temp
	else:
		temp = li[k]
print(x)
import sys
n=int(sys.stdin.readline())
li = [0] * n
for i in range(n):
	li[i] = int(sys.stdin.readline())
li.sort()
answer = 0
for x in range(n):
	temp = li[x] * (n-x)
	if temp > answer:
		answer = temp
		
print(answer)
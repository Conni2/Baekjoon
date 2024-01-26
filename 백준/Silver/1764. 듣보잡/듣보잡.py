import sys
n, m = map(int, sys.stdin.readline().split())
no_heard = {}
for i in range (n):
    x = sys.stdin.readline()[:-1]
    no_heard[x] = 0

for r in range(m):
    t = sys.stdin.readline()[:-1]
    if t in no_heard:
        no_heard[t] = 1

answer = list(key for key, value in no_heard.items() if value == 1)
answer.sort()
print(len(answer))
print(*answer, sep='\n')
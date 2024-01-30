import sys
n, k = map(int, sys.stdin.readline().split())
wallet = [0] * n
for i in range(n):
	wallet[i] = int(sys.stdin.readline())
answer = 0
wallet.sort(reverse=True)
i = 0
while k != 0:
    while k >= wallet[i]:
        answer += k // wallet[i]
        k = k % wallet[i]
    i += 1

print(answer)
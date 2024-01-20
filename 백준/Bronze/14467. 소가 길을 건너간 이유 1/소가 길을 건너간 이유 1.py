import sys
case = int(sys.stdin.readline())
cows = {}
ans = 0
for i in range(case):
    num, cross = map(int, sys.stdin.readline().split())
    if num not in cows:
        cows[num] = cross
    else:
        if cows[num] != cross:
            ans += 1
            cows[num] = cross

print(ans)
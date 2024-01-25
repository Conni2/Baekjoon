import sys
n, t, p = map(int, sys.stdin.readline().split())
if n == 0:
    print(1)
    sys.exit()
scores = list(map(int, sys.stdin.readline().split()))
scores.append(t)
scores.sort(reverse = True)
rank = scores[:p]
if t in rank:
    if len(scores) > p and t == scores[p]:
        print(-1)
    else:
        print(rank.index(t)+1)
else:
    print(-1)
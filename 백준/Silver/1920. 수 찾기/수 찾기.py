import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

mapp ={}
for i in range(len(A)):
    mapp[A[i]] = 0

for j in range(M):
    if compare[j] not in mapp:
        print('0')
    else:
        print('1')
import sys
n = int(sys.stdin.readline())
for i in range(n*5):
    if i <= n-1:
        print('@'*(n*5))
    else:
        print('@'*n)
import sys
n = int(sys.stdin.readline())
for i in range(n*5):
    if 0<=i<=n-1 or (4*n)<=i<=(n*5-1):
        print('@'*(n*5))
    else:
        print('@'*n)
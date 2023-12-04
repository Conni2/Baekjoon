import sys
n = int(sys.stdin.readline())
for i in range(n*5):
    if i  <= (4*n-1):
        print('@'*n)
    else:
        print('@'*(n*5))
import sys
n = int(sys.stdin.readline())
for i in range(n*5):
    if 0<=i<=n-1:
        print('@'*(n*3)+' '*n+'@'*n)
    elif (4*n)<=i<=(n*5-1):
        print('@'*n+' '*n+'@'*(n*3))
    else:
        print(('@'*n+' '*n)*2+'@'*n)
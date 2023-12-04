import sys
n = int(sys.stdin.readline())
for i in range(n*5):
    if 0<=i<=(n-1) or (4*n)<=i<=(n*5-1):
        print('@'*n+' '*(3*n)+'@'*n)
    elif (2*n)<=i<=(3*n-1):
        print('@'*(3*n))
    else:
        print('@'*n+' '*(2*n)+'@'*n)
import sys
case = int(sys.stdin.readline())
for x in range(case):
    count = 0
    n, m = map(int,sys.stdin.readline().split())
    for y in range(n, m+1):
        num = str(y)
        count += num.count('0')
    print(count)
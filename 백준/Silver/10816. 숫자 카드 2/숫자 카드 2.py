import sys
geun_case = int(sys.stdin.readline())
geun = list(map(int, sys.stdin.readline().split()))
compare_case = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

count = {}
for i in geun:
    try: count[i] += 1
    except: count[i]=1

for j in range(compare_case):
    if compare[j] not in count:
        print(0, end=' ')
    else:
        print(count[compare[j]], end=' ')
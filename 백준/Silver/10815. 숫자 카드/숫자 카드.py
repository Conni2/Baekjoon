import sys
geun_case = int(sys.stdin.readline())
geun = list(map(int, sys.stdin.readline().split()))
compare_case = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

mapp ={}
for i in range(len(geun)):
    mapp[geun[i]] = 0

for j in range(compare_case):
    if compare[j] not in mapp:
        print(0, end=' ')
    else:
        print(1, end=' ')
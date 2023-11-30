import sys
n,m = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
count = 0
left = 0
right = 1

while right <= n and left <= right:
    part_nums = num[left:right]
    total = sum(part_nums)
    if total == m:
        count += 1
        left += 1
    elif total < m:
        right += 1
    else:
        left += 1

print(count)
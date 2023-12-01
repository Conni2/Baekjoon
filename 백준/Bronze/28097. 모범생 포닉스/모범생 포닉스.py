import sys

n = int(sys.stdin.readline())
study = list(map(int,sys.stdin.readline().split()))
term = len(study)-1
total = sum(study)+8*term
date = total // 24
time = total % 24
print('{} {}'.format(date, time))
import sys
num = list(sys.stdin.readline()[:-1])
num = sorted(num, reverse=True)
print(''.join(num))
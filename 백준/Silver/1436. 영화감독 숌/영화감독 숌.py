import sys
n = int(sys.stdin.readline())
count = 0
x = 666
while True:
    if '666' in str(x):
        count += 1
    if count == n:
        break
    x += 1
print(x)
import sys

product, k = map(int,sys.stdin.readline().split())

for i in range(2, k):
    if product % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")
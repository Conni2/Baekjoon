import sys
num = int(sys.stdin.readline())
x = num // 3 + num % 3
if x % 2 == 0:
    print("CY")
else:
    print("SK")
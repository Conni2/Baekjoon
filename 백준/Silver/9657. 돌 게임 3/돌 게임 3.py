import sys
num = int(sys.stdin.readline())
if num % 7 == 0 or num % 7 == 2:
    print("CY")
else:
    print("SK")
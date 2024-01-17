import sys
a,b,c,x,y = map(int, sys.stdin.readline().split())
left = 0
if x < y:
    left = (y-x) * b
elif x > y :
    left = (x-y) * a
case_without = a*x + b*y
case_with = min((x, y))*c*2 + left
case_banban = max((x, y))*c*2

print(min(case_without, case_with, case_banban))
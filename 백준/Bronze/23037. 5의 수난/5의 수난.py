import sys
five = sys.stdin.readline()
result = 0
for i in range(5):
    result += int(five[i])**5

print(result)
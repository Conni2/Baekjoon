import sys
import math

sugar = int(sys.stdin.readline())
result = math.floor(sugar / 5)
after_five = (sugar - (5*result))
if after_five % 3 == 1 and sugar > 5:
    result += (after_five + 5) // 3
    result -= 1
    print(result)
elif after_five % 3 == 2 and sugar > 7:
    result += (after_five + 10) // 3
    result -= 2
    print(result)
elif after_five % 3 == 0:
    result += (after_five) // 3
    print(result)
else:
    print(-1)
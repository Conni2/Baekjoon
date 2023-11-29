import math
x = int(input())
for i in range(1, x*2+1):
    stars_odd = math.ceil(x / 2)
    stars_even = x // 2
    if i % 2 == 1:
        print("* "*stars_odd)
    else:
        print(" *"*stars_even)
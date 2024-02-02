import sys
import math
ds = sys.stdin.readline()[:-1]
count = 0
for i in range(1, len(ds)):
    if ds[i] != ds[i-1]:
        count +=1
        
print(math.ceil(count/2))
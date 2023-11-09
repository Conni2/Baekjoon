x = int(input())
n = len(str(x))
nines = 0
for i in range(1, n):
    nines += 9 * (10**(i-1)) * i
print((x-(10**(n-1))+1)*n + nines)
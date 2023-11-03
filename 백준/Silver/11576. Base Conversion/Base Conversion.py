a, b = map(int, input().split(' '))
n = int(input())
anum = list(map(int, input().split(' ')))
ship = 0
for i in range(n):
    ship += anum[i]*(a**(n-i-1))
bnum = []
while True:
    rem = ship % b
    ship = ship//b
    bnum.append(str(rem))
    if ship < b:
        bnum.append(str(ship))
        break
bnum.reverse()
print(' '.join(bnum))
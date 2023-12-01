n, m = map(int, input().split())
ttorm_to_dordom = []
dordom = []
for x in range (n):
    tt = input()
    ttorm =''
    for i in range (m):
        ttorm += str(tt[i])*2
    ttorm_to_dordom.append(ttorm)
for y in range(n):
    dordom.append(input())
z = 0
while z < n:
    if ttorm_to_dordom[z] != dordom[z]:
        print('Not Eyfa')
        break
    else:
        if z == n-1:
            print('Eyfa')
            break
        z += 1
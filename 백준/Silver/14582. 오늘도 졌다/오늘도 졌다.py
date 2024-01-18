import sys
woolim = list(map(int, sys.stdin.readline().split()))
startlink = list(map(int, sys.stdin.readline().split()))
woo = 0
st = 0
for i in range(1, 19):
    if i % 2 == 1:
        woo += woolim[(i-1)//2]
    else:
        st += startlink[(i-2)//2]
    if woo > st:
        print('Yes')
        break
    elif i == 18:
        print('No')
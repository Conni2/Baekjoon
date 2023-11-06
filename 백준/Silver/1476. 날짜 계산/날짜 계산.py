e,s,m = map(int,input().split())
n = 1
while True:
    if (n-e)%15 == 0 and (n-m)%19 == 0 and (n-s)%28 == 0:
        break
    n += 1

print(n)
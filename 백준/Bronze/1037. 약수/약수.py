rfn = int(input())
rf = list(map(int, input().split()))
rf = sorted(rf)
if rfn % 2 == 1:
    print(rf[(rfn-1)//2] ** 2)
else:
    print(max(rf)*min(rf))
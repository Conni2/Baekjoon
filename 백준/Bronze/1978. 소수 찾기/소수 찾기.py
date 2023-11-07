cas = int(input())
numbers = list(map(int, input().split()))
prime = 0
for i in range(cas):
    factor = 0
    for x in range(1, numbers[i]+1):
        if numbers[i] % x == 0:
            factor += 1
    if factor == 2:
        prime += 1

print(prime)
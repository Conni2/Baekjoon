game = int(input())
i = 0
c = 100
s = 100
while i < game:
    #map(function, iterable)
    a, b = map(int, input().split(' '))
    if a < b:
        c -= b
    elif a > b:
        s -= a
    i += 1
print('{}\n{}'.format(c,s))

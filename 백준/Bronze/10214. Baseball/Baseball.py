game = int(input())
y = 0
k = 0
x = 0
while x < game:
    i = 0
    while i < 9:
        #map(function, iterable)
        a, b = map(int, input().split(' '))
        y += a
        k += b
        i += 1
    if y > k:
        print('Yonsei')
    elif y == k:
        print("Draw")
    else:
        print("Korea")
    x += 1
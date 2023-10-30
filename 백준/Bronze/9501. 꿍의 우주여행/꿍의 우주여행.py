case = int(input())
i = 0
while i < case:
    n, d = map(int, input().split(' '))
    spaceship = 0
    for x in range(n):
        v, f, c = map(int, input().split(' '))
        if v*f//c >= d:
            spaceship += 1
    print(spaceship)
    i += 1
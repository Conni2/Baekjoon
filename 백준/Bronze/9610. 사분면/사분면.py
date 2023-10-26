tries = int(input())
one = 0
two = 0
three = 0
four = 0
axis = 0
i = 0
while i < tries:
    ab = input().split(' ')
    a = int(ab[0])
    b = int(ab[1])
    times = a*b
    if times == 0:
        axis += 1
    elif times > 0:
        if a > 0:
            one += 1
        else:
            three += 1
    else:
        if a < 0:
            two += 1
        else:
            four += 1
    i += 1

print('Q1: {}\nQ2: {}\nQ3: {}\nQ4: {}\nAXIS: {}'.format(one, two, three, four, axis))
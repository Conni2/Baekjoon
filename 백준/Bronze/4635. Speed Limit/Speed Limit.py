while True:
    sets = int(input())
    if sets == -1:
        break
    distance = 0
    temp = 0
    for i in range(sets):
        v, t = map(int, input().split(' '))
        distance += v*(t-temp)
        temp = t
    print("{} miles".format(distance))
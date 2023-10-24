tries = int(input())
i = 0
while i < tries:
    rec = input().split(' ')
    r = int(rec[0])
    e = int(rec[1])
    c = int(rec[2])
    if r < e-c:
        print("advertise")
    elif r == e-c:
        print('does not matter')
    else:
        print('do not advertise')
    i+=1
tries = int(input())
i = 0
while i < tries:
    order = input().split(' ')
    times = int(order[0])
    ele = list(order[1])
    #TIL; join 안에서 for 문 쓸 수 있음
    print(''.join(x*times for x in ele))
    i+=1
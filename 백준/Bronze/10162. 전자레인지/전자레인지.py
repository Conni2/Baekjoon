t = int(input())
a = t // 300
b = (t % 300) // 60
c = ((t % 300) % 60) // 10
if ((t % 300) % 60) % 10 != 0:
    print(-1)
else:
    print('{} {} {}'.format(a, b, c))
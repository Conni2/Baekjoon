game = int(input())
y = 0
k = 0
x = 0
top_s = ''
top_c = 0
while x < game:
    i = 0
    school = int(input())
    while i < school:
        sc = input().split(' ')
        s = sc[0]
        c = int(sc[1])
        if top_c < c:
            top_c = c
            top_s = s
        i += 1
    print(top_s)
    x+=1
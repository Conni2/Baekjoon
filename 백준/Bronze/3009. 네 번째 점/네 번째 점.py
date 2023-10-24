a = input().split(' ')
b = input().split(' ')
c = input().split(' ')
d = []
for i in range(len(a)):
    if a[i] == b[i]:
        d.append(c[i])
    elif b[i] == c[i]:
        d.append(a[i])
    else:
        d.append(b[i])

print(d[0]+' '+d[1])
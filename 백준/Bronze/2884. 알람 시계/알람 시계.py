hm = input().split(' ')
h = int(hm[0])
m = int(hm[1])
if h == 0:
    h = 24
minutes = h*60 + m - 45
h = minutes // 60
m = minutes % 60
if h == 24:
    h = 0
print(str(h)+" "+str(m))
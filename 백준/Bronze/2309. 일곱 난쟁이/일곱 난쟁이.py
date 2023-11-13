import sys
nj = []
totnj = 0
for i in range(9):
    nan = int(sys.stdin.readline())
    nj.append(nan)
    totnj += nan
totnj -= 100

nj.sort()

def fake():
    for i in range(len(nj)):
        for x in range(i+1, len(nj)):
            sumnj = nj[i] + nj[x]
            if sumnj == totnj:
                return(i, x)
            
a, b = fake()
del nj[a]
del nj[b-1]

for i in range(len(nj)):
    print(nj[i])
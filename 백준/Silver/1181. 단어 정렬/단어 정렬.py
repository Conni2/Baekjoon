import sys
N = int(sys.stdin.readline())
dic ={}

for i in range(N):
    word = sys.stdin.readline()[:-1]
    dic[word] = len(word)

dic = sorted(dic.items(), key = lambda x: (x[1], x[0]))

for r in range(len(dic)):
    print(dic[r][0])
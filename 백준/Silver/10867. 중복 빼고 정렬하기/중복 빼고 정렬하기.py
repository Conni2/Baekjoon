import sys
N = int(sys.stdin.readline())
string = list(map(int,sys.stdin.readline().split()))
dic ={}

for i in string:
    dic[i] = 0

dic = sorted(dic)

print(" ".join(map(str, dic)))
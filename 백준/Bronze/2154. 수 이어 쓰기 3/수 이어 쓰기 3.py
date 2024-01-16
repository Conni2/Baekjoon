import sys
n = int(sys.stdin.readline())
string = ""
for i in range(1, n+1):
    string += str(i)
print(string.index(str(n))+1)
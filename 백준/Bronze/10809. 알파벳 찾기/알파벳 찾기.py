import sys
import string
s = list(sys.stdin.readline()[:-1])
lower = [i for i in string.ascii_lowercase]
for i in lower:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')
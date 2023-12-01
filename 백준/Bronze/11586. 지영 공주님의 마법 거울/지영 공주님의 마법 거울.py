import sys
n = int(sys.stdin.readline())
mirror = []
for i in range(n):
    line = input()
    mirror.append(line)
k = int(sys.stdin.readline())
if k == 1:
    for x in range(n):
        print(mirror[x])
elif k == 3:
    for x in range(n-1, -1, -1):
        print(mirror[x])
else:
    for x in range(n):
        word = list(mirror[x])        
        for left in range(n//2):
            right = n - left - 1
            temp = word[left]
            word[left] = word[right]
            word[right] = temp
            reverse = ''.join(word)
        print(reverse)
import sys
korea = list(sys.stdin.readline())
sample = ['K','O','R','E','A']
count = 0
x = 0
for i in range(len(korea)):
    if korea[i] == sample[(x%5)]:
        x += 1
        count += 1
print(count)

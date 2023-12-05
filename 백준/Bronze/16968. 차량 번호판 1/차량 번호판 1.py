import sys
form = list(sys.stdin.readline()[:-1])
total = 0
if form[0] == 'c':
    total = 26
else:
    total = 10

for i in range(1, len(form)):
    if form[i] == 'c':
        if form[i-1] == 'c':
            total *= 25
        else:
            total *= 26
    else:
        if form[i-1] == 'd':
            total *= 9
        else:
            total *= 10

print(total)
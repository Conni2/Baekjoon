import sys
form = sys.stdin.readline()[:-1]
rule = {'c':26, 'd':10}
total = rule[form[0]]

for i in range(1, len(form)):
    num = rule[form[i]]
    if form[i] == form[i-1]:
        num -= 1
    total *= num
    total %= 1000000009

print(total)
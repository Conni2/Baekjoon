import sys
case = list(sys.stdin.readline()[:-1].upper())
if len(case) == 1:
    print(case[0])
    sys.exit()

alphs = list(set(case))
answer = 0
dup = 0
for i in range(1, len(alphs)):
    if case.count(alphs[i]) > case.count(alphs[answer]):
        answer = i
        dup = 0
    elif case.count(alphs[i]) == case.count(alphs[answer]):
        dup = 1

if dup == 0:
    print(alphs[answer])
elif dup == 1:
    print("?")
import sys
def great(a,b):
    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b%i == 0:
            return(i)

case = int(input())
for i in range(case):
    numbers = list(map(int,sys.stdin.readline().split()))
    gcd = 0
    for x in range(1,len(numbers)-1):
        a = numbers[x]
        for y in range(x+1, len(numbers)):
            b = numbers[y]
            gx = great(a,b)
            gcd += gx
    print(gcd)

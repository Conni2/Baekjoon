def gcd(a,b):
    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b%i == 0:
            return(i)
tries = int(input())
i = 0
while i < tries:
    a, b = map(int, input().split(' '))
    x = gcd(a,b)
    print(a//x*b//x*x)
    i+=1
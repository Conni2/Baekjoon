def prime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

t, p = map(int, input().split())

for i in range(t, p+1):
    if prime(i):
        print(i)
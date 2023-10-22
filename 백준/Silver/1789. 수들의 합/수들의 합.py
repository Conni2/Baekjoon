s = int(input())
n = 1

while True:
    sum = (n**2 + n) // 2
    if sum < s:
        n += 1
    elif sum == s:
        print(n)
        break
    else:
        print(n-1)
        break
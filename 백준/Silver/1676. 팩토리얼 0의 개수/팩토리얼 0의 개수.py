n = int(input())
zeros = 0
i = 1
while True:
    fives = n // (5**i)
    if fives == 0:
        break
    zeros += fives
    i += 1

print(zeros)
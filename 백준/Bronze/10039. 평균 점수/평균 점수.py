i = 0
sum = 0
while i < 5:
    x = int(input())
    if x < 40:
        x = 40
    sum += x
    i += 1
print(sum//5)
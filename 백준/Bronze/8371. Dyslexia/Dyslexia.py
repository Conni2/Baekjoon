character = int(input())
a = list(input())
b = list(input())
count = 0
for i in range(character):
    if a[i] != b[i]:
        count += 1
print(count)
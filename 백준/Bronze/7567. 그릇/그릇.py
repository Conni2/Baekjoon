dish = list(input())
top = 10
i = 1
while i < len(dish):
    x = i-1
    if dish[i] == dish[x]:
        top += 5
    else:
        top += 10
    i += 1
print(top)
abc = input().split(" ")
ascending = []
for i in range(len(abc)):
    ascending.append(int(abc[i]))
ascending.sort()
print(ascending[-2])
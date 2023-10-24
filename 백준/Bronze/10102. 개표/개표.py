judge = int(input())
votes = list(input())
a = 0
for i in range(len(votes)):
    if votes[i] == "A":
        a += 1
    i += 1
b = judge - a
if a > b:
    print("A")
elif a == b:
    print('Tie')
else:
    print('B')
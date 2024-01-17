import sys
quiz = []
for i in range(8):
    x = int(sys.stdin.readline())
    quiz.append(x)

highest = sorted(quiz, reverse=True)
highest = highest[:5]
print(sum(highest))

indexes = []
for i in range(5):
    indexes.append(1+quiz.index(highest[i]))
indexes.sort()

for i in range(5):
    print((indexes[i]), end=" ")
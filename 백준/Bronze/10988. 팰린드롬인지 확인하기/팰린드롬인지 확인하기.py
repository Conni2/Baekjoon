word = list(input())
reverse_word = []
for i in range(1, len(word)+1):
    reverse_word.append(word[-i])
drow = ''.join(reverse_word)
word = ''.join(word)
if drow == word:
    print(1)
else:
    print(0)
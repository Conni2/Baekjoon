import sys
word = input()
word_list = list(word)
reverse = ""
for left in range(len(word_list)//2):
    right = len(word_list) - left - 1
    temp = word_list[left]
    word_list[left] = word_list[right]
    word_list[right] = temp            
    reverse = ''.join(word_list)
if len(word) ==1:
    print("true")
elif reverse == word:
    print("true")
else:
    print("false")
# 문자열에서 특정 문자 지우는 건 문자열.replace('원래있던것을', '바꾸고 싶은 것으로')
# 예를 들어 문자열.replace('old', 'new') 면 old 라는 문자열 내의 문자열을 찾아서 new라는 문자열로 바꿔버림
import sys
word = sys.stdin.readline()[:-1]
cro_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cro_count = 0
for i in range(len(cro_alphabet)):
    cro_alph_count = word.count(cro_alphabet[i])
    if cro_alph_count != 0:
        cro_count += cro_alph_count
        word = word.replace(str(cro_alphabet[i]), " ")
word = word.replace(" ", "")
alph_count = len(word)
print(cro_count + alph_count)
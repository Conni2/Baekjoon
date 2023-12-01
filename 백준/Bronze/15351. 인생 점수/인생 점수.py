#ord 함수 = unicode 나타냄. 대문자 A는 65부터 시작
case = int(input())
for z in range(case):
    life = list(input())
    score = 0
    for i in range(len(life)):
        if life[i] == ' ':
            score += 0
        else:
            score += ord(life[i])-64
    if score == 100:
        print("PERFECT LIFE")
    else:
        print(score)
while True:
    number = int(input())
    if number == -1:
        break
    factor = []
    f = 1
    while f < number:
        if number % f == 0:
            factor.append(f)
        f += 1
    #TIL: sum(iterable) 가능
    if sum(factor) == number:
        #TIL: '구분자'.join(리스트) i.e '_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환
        #TIL: list의 요소를 한 줄에 하나씩 출력하고 싶다면? -> sep='\n'를 쓰면 된다. (seperator)
        #지금 list 내의 자료형이 int 이기 때문에 join 안에서 for 문써서 str로 바꿔야함
        print(str(number)+' = '+' + '.join(str(f) for f in factor))
    else:
        print('{} is NOT perfect.'.format(number))
while True:
    user = input()
    if user == '0 0':
        break
    ab = user.split(' ')
    a = int(ab[0])
    b = int(ab[1])
    if a % b == 0:
        print('multiple')
    elif b % a == 0:
        print('factor')
    else:
        print('neither')
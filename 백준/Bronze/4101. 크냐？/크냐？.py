while True:
    ab = input()
    if ab == '0 0':
        break
    ab = ab.split(' ')
    if int(ab[0]) > int(ab[1]):
        print('Yes')
    else:
        print('No')
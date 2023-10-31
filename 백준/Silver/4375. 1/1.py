#EOFError: use while True try:, except EOFError: break
while True:
    try:
        n = int(input())
        i = 0
        ones = 0
        while True:
            ones += 10**i
            if ones % n == 0:
                print(i+1)
                break
            i += 1
    except EOFError:
        break
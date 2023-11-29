x = int(input())
side = 4*(x-1)+1
for i in range(1, (side+1)//2+1):
    if i % 2 == 1:
        n = (i+1)//2
        print('* '*(n-1) + '*'* (side-(4*(n-1))) +' *'*(n-1))
    else:
        e = i//2
        print('* '*(e) + ' '* (side-2*i) +' *'*(e))
for i in range((side+1)//2-1, 0, -1):
    if i % 2 == 1:
        n = (i+1)//2
        print('* '*(n-1) + '*'* (side-(4*(n-1))) +' *'*(n-1))
    else:
        e = i//2
        print('* '*(e) + ' '* (side-2*i) +' *'*(e))
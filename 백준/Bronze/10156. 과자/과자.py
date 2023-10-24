knm = input().split(' ')
parents = int(knm[0])*int(knm[1])-int(knm[2])
if parents > 0:
    print(parents)
else:
    print(0)
tries = int(input())
i=1
while i < tries+1:
    ab = input().split(" ")
    print("Case #{}: {} + {} = {}".format(i, ab[0], ab[1], int(int(ab[0])+int(ab[1]))))
    i +=1
classes = int(input())
for i in range(classes):
    score = list(map(int, input().split()))
    del score[0]
    score = sorted(score, reverse = True)
    maxi = score[0]
    mini = score[-1]
    gap = 0
    for x in range(len(score)-1):
        subs = score[x] - score[x+1]
        if subs > gap:
            gap = subs
    print("Class {}".format(i+1))
    print("Max {}, Min {}, Largest gap {}".format(maxi, mini, gap))
ppl = int(input())
i = 0
prize = []
while i < ppl:
    abc = input().split(' ')
    if abc[0] == abc[1] and abc[0] == abc[2]:
        prize.append(10000+int(abc[0])*1000)
    elif abc[0] == abc[1] or abc[0] == abc[2]:
        prize.append(1000+int(abc[0])*100)
    elif abc[1] == abc[2]:
        prize.append(1000+int(abc[2])*100)
    else:
        prize.append(int(max(abc))*100)
    i+=1
print(max(prize))
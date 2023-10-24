abc = input().split(' ')
if abc[0] == abc[1] and abc[0] == abc[2]:
    print(10000+int(abc[0])*1000)
elif abc[0] == abc[1] or abc[0] == abc[2]:
    print(1000+int(abc[0])*100)
elif abc[1] == abc[2]:
    print(1000+int(abc[2])*100)
else:
    print(int(max(abc))*100)
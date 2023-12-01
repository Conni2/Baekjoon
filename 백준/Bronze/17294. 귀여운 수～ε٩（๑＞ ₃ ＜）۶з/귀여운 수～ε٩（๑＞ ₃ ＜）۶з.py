import sys
qt = list(map(int, sys.stdin.readline()[:-1]))
count = 0
if len(qt) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    standard = qt[0] - qt[1]
    for i in range(1, len(qt)-1):
        if qt[i] - qt[i+1] != standard:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            break
        else:
            count += 1
    if count == len(qt) - 2:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
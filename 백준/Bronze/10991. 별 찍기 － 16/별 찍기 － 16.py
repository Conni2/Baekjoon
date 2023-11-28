x = int(input())
for i in range (1, x+1):
    if i == 1:
        print(" "*(x-1)+"*")
    else:
        space = ""
        for z in range(1, 2*i-2):
            if z % 2 == 1:
                space += " "
            else:
                space += "*"
        print(" "*(x-i)+"*"+space+"*")
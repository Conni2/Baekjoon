case = int(input())
i = 0
while i < case:
    formula = input().split(" ")
    number = float(formula[0])
    del formula[0]
    for f in range(len(formula)):
        if formula[f] == "@":
            number *= 3
        elif formula[f] == "%":
            number += 5
        else:
            number -= 7
    print(format(number, ".2f"))
    i += 1
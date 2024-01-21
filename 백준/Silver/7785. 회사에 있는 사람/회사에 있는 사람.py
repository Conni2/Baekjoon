import sys
case = int(sys.stdin.readline())
company = {}
for i in range(case):
    name, status = sys.stdin.readline().split()
    if name in company and status == "leave":
        del company[name]
    elif name not in company and status == "enter":
        company[name] = status

yageun = sorted(company, reverse = True)
for i in range(len(yageun)):
    print(yageun[i])
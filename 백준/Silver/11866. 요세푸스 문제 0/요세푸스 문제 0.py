import sys
n, k = map(int, sys.stdin.readline().split())
member = list(range(1, n+1))
yosepus = []
will_be_deleted = 0
while member:
    will_be_deleted += k-1
    if will_be_deleted >= len(member):
        will_be_deleted %= len(member)
    yosepus.append(str(member.pop(will_be_deleted)))
print("<{}>".format(', '.join(yosepus)))
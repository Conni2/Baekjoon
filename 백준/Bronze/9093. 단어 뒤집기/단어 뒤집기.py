import sys

case = int(input())

for i in range(case):
    task = list(sys.stdin.readline().split())
    for x in range(len(task)):
        if len(task[x]) > 1:
            temporary = list(task[x])
            for left in range(len(temporary)//2):
                right = len(temporary) - left - 1
                temp = temporary[left]
                temporary[left] = temporary[right]
                temporary[right] = temp
            task[x] = ''.join(temporary)
    print(' '.join(task))
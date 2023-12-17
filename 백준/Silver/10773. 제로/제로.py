import sys
case = int(sys.stdin.readline())
nums = []
for i in range(case):
    input = int(sys.stdin.readline())
    if input == 0:
        if len(nums) != 0:
            nums.pop()
    else:
        nums.append(input)
print(sum(nums))
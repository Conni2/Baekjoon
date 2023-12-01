#리스트에 여러개의 항목 넘겨줄 때에는 리스트 형태로 묶은 후 append가 아니라 extend 메소드 사용
case = int(input())
palindrome = list(input().split())

check = []
for i in range(case):
    first = palindrome[i][0]
    last = palindrome[i][-1]
    check.extend([first, last])

error = check.count(check[0])
if error == len(check):
    print(1)
else:
    print(0)
voters = int(input())
i = 0
total = 0
while i < voters:
    vote = int(input())
    total += vote
    i += 1
if total > voters/2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
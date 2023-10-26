tries = int(input())
t = 0
while t < tries: 
    answer = input()
    x = answer.split('X')
    os = 0
    for i in range(len(x)):
        os += (len(x[i])*(len(x[i])+1))//2
        i+=1
    print(os)
    t += 1
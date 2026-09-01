t= int(input())
 
for _ in range(t):
    n = int(input())
    if n<=2:
        answer=0
    elif n%2 == 0:
        answer= n//2 -1
    else:
        answer= n//2
    print(answer)
t = int(input())
 
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
 
    wrong = []
 
    for i in range(n):
        if p[i] != i + 1:
            wrong.append(p[i])
 
    if wrong == sorted(wrong, reverse=True):
        print("YES")
    else:
        print("NO")
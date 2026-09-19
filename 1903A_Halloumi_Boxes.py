t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    if k > 1:
        print("YES")
    elif a == sorted(a):
        print("YES")
    else:
        print("NO")
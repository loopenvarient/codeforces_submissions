t = int(input())
 
for _ in range(t):
    s = input()
 
    a = list(map(int, s))
 
    if sum(a[:3]) == sum(a[3:]):
        print("YES")
    else:
        print("NO")
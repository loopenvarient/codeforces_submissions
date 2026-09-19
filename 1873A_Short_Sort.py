t = int(input())
 
for i in range(t):
    s = input()
 
    if s == "abc" or s == "acb" or s == "bac" or s == "cba":
        print("YES")
    else:
        print("NO")
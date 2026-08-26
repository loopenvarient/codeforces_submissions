n = int(input())
s = input().lower()
 
letters = set("abcdefghijklmnopqrstuvwxyz")
 
if letters.issubset(set(s)):
    print("YES")
else:
    print("NO")
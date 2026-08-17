n = int(input())
 
count = 1
previous = input()
 
for i in range(n - 1):
    s = input()
 
    if s != previous:
        count += 1
 
    previous = s
 
print(count)
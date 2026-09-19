n = int(input())
a = list(map(int, input().split()))
 
high = low = a[0]
count = 0
 
for x in a[1:]:
    if x > high:
        high = x
        count += 1
    elif x < low:
        low = x
        count += 1
 
print(count)
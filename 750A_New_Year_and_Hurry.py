n, k = map(int, input().split())
 
time = 240 - k
solved = 0
 
for i in range(1, n + 1):
    time -= 5 * i
 
    if time < 0:
        break
 
    solved += 1
 
print(solved)
 
 
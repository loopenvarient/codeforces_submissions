n = int(input())
 
teams = []
 
for _ in range(n):
    home, away = map(int, input().split())
    teams.append((home, away))
 
answer = 0
 
for i in range(n):
    for j in range(n):
        if i != j and teams[i][0] == teams[j][1]:
            answer += 1
 
print(answer)
 
 
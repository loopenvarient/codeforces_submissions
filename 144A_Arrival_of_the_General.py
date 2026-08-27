n = int(input())
a = list(map(int, input().split()))
 
max_index = a.index(max(a))
min_index = len(a) - 1 - a[::-1].index(min(a))
 
if max_index < min_index:
    answer = max_index + (n - 1 - min_index)
else:
    answer = max_index + (n - 1 - min_index) - 1
 
print(answer)
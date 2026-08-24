t = int(input())
 
for _ in range(t):
    n = int(input())
 
    result = []
    place = 1
 
    while n > 0:
        digit = n % 10
 
        if digit != 0:
            result.append(digit * place)
 
        n //= 10
        place *= 10
 
    print(len(result))
    print(*result)
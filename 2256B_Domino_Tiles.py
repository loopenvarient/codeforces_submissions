MOD = 998244353
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
 
    dp = [[0] * 2 for _ in range(2)]
 
    for a in range(2):
        if s[0] == '?' or int(s[0]) == a:
            for b in range(2):
                if s[1] == '?' or int(s[1]) == b:
                    dp[a][b] += 1
 
    for i in range(2, n):
        new = [[0] * 2 for _ in range(2)]
 
        for a in range(2):
            for b in range(2):
                if dp[a][b] == 0:
                    continue
 
                for c in range(2):
                    if s[i] != '?' and int(s[i]) != c:
                        continue
 
                    # Key condition:
                    # c must be different from a
                    if c == a:
                        continue
 
                    new[b][c] += dp[a][b]
                    new[b][c] %= MOD
 
        dp = new
 
    answer = sum(map(sum, dp)) % MOD
    print(answer)
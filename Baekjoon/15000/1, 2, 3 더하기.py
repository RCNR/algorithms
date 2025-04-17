# 1, 2, 3 더하기 3 15988
import sys
input = sys.stdin.readline

dp = [0] * (1000003)

n = int(input())
MOD = 1000000009

dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000003):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % MOD

for _ in range(n):
    k = int(input())
    print(dp[k])
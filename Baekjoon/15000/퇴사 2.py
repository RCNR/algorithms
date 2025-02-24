# 퇴사2 15486
import sys
input = sys.stdin.readline

n = int(input())
T = [0] * (n + 3)
P = [0] * (n + 3)
dp = [0] * (n + 3)
for i in range(1, n+1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

for i in range(n, 0, -1):
    if T[i] + i - 1 < n+1:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(max(dp))
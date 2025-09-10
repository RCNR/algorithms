# 템포럴 그래프.py 25953
# 최단 거리 - 다익스트라 사용하면 된다. 다익스트라는 MlogN
# 그런데 여기서 M이 천만이다. -> 시간초과 날 것임
# 어떤 상태가 i에서 i+1로 넘어가고, 방향성이 있으며 다시 되돌아 갈 수 없다
# -> dp 이용

import sys
input = sys.stdin.readline

N, T, M = map(int, input().split())
s, e = map(int, input().split())

adj = [[] for _ in range(T+1)]
INF = int(10e9)

dp = [[INF] * N for _ in range(T+1)]

for i in range(1, T+1):
    for j in range(M):
        u, v, cost = map(int, input().split())
        adj[i].append([u, v, cost])

dp[0][s] = 0

for i in range(1, T+1):
    for j in range(N):
        dp[i][j] = dp[i-1][j]

    for nxt in adj[i]:
        st, end, cost = nxt
        # print("st, end, cost = ", st, end, cost)

        dp[i][st] = min(dp[i-1][end] + cost, dp[i][st])
        dp[i][end] = min(dp[i-1][st] + cost, dp[i][end])


if dp[T][e] == INF:
    print(-1)
else: print(dp[T][e])


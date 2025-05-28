# 2637 장난감 조립
import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
m = int(input())

adj = [[] for _ in range(n+3)]
q = deque()
indegree = [0] * (n+3)

for _ in range(m):
    x, y, z = map(int, input().split())
    adj[y].append((x, z))
    indegree[x] += 1

board = [[0] * (n+2) for _ in range(n+2)]
res = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        board[i][i] = 1
        res.append(i)

while q:
    cur = q.popleft()
    for num,cnt in adj[cur]:
        for i in range(1, n+1):
            board[num][i] += board[cur][i] * cnt
        indegree[num] -= 1
        if indegree[num] == 0: q.append(num)

for i in res:
    print(i, board[n][i])
# 바닥 장식.py 1388
# 빡구현

import sys
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
cnt = 0
is_visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == '-' and not is_visited[i][j]:
            is_visited[i][j] = True
            for k in range(j, m):
                if board[i][k] == '-': is_visited[i][k] = True
                else: break
            cnt += 1

for j in range(m):
    for i in range(n):
        if board[i][j] == '|' and not is_visited[i][j]:
            is_visited[i][j] = True
            for k in range(i, n):
                if board[k][j] == '|': is_visited[k][j] = True
                else: break
            cnt += 1

print(cnt)
# 전쟁 - 전투.py 1303
# DFS, BFS를 써서 같은 팀이 인접한 칸을 모두 탐색한 뒤
# 병사의 수를 세서 제곱하여 더해준다.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = list(input().rstrip() for _ in range(m))
is_visited = [[False] * n for _ in range(m)]

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

res_w = []
res_b = []

def dfs(x, y, team):
    move = 1

    if team != board[x][y]:
        return

    is_visited[x][y] = True

    for dir in range(4):
        nx = dx[dir] + x
        ny = dy[dir] + y

        if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
        if team != board[nx][ny] or is_visited[nx][ny]: continue

        
        move += dfs(nx, ny, team)

    return move

res_w = 0
res_b = 0

for i in range(m):
    for j in range(n):
        if not is_visited[i][j]:
            cnt = dfs(i, j, board[i][j])

            if board[i][j] == 'W':
                res_w += cnt ** 2
            else:
                res_b += cnt ** 2

print(res_w, res_b)
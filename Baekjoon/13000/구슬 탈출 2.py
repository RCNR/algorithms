# 구슬 탈출 2 13460
# 구슬 2개를 동시에 bfs로 움직이기
# 빨간 공을 방향으로 끝까지 이동
# 파란 공을 방향으로 끝까지 이동
# 파란 공이 구멍에 빠지면 실패
# 빨간 공이 구멍에 빠지면 성공
# 둘 다 같은 칸애 멈췄다면 위치 조정
# 10번 이상 이동하는 경우 패스

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
is_visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

def move(x, y, dir): # 공 이동
    cnt = 0 # 몇 칸 움직였나
    while board[x + dx[dir]][y + dy[dir]] != '#' and board[x][y] != 'O':
        x += dx[dir]
        y += dy[dir]
        cnt += 1
    
    return x, y, cnt
    


rx, ry = 0, 0
bx, by = 0, 0
holex, holey = 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R': rx, ry = i, j
        elif board[i][j] == 'B': bx, by = i, j
        elif board[i][j] == 'O': holex, holey = i, j

Q = deque()
Q.append((rx, ry, bx, by, 0))
is_visited[rx][ry][bx][by] = True

while Q:
    cur_rx, cur_ry, cur_bx, cur_by, depth = Q.popleft()

    if depth >= 10: continue

    for dir in range(4):
        n_rx, n_ry, r_cnt = move(cur_rx, cur_ry, dir)
        n_bx, n_by, b_cnt = move(cur_bx, cur_by, dir)

        if n_bx == holex and n_by == holey: continue

        if n_rx == holex and n_ry == holey:
            print(depth + 1)
            exit(0)

        if n_rx == n_bx and n_ry == n_by:
            if r_cnt > b_cnt: # 빨간공이 더 뒤에 있었던 경우
                n_rx -= dx[dir]
                n_ry -= dy[dir]
            else:             # 파란공이 더 뒤에 있었던 경우
                n_bx -= dx[dir]
                n_by -= dy[dir]
        
        if is_visited[n_rx][n_ry][n_bx][n_by]: continue
  

        is_visited[n_rx][n_ry][n_bx][n_by] = True
        Q.append((n_rx, n_ry, n_bx, n_by, depth + 1))

print(-1)
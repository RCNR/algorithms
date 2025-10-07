# 연구소.py 14502
# 벽 3개 세우기 -> DFS로 바이러스 퍼트리기 -> 안전 영역 카운트하기
# 벽 3개 세우는 경우 -> 모든 경우 수 구하기 -> 3중 fo문 O((n*m)^3)
# DFS로 바이러스 퍼트리기 -> O(n*m)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))

wall = []
virus = []
res = 0
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]


def dfs(x, y):

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if is_visited[nx][ny] == True: continue
        if board[nx][ny] == 1: continue # 벽인 경우 제외

        is_visited[nx][ny] = True
        dfs(nx, ny)

   

# 바이러스 퍼트리기 코드
def func():

    global is_visited
    is_visited = [[False] * m for _ in range(n)]

    v_length = len(virus)
    for i in range(v_length):
        x, y = virus[i]
        is_visited[x][y] = True
        dfs(x, y)
    

    # 퍼트려진 바이러스 후에 안전 영역 카운트하기 코드
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and is_visited[i][j] == False:
                cnt += 1
    # if cnt == 13:
    #     print(board)
    #     print(is_visited)

    
    return cnt

for i in range(n):
    for j in range(m):
        if board[i][j] == 0: wall.append((i, j)) # 벽이 아닌 경로
        if board[i][j] == 2: virus.append((i, j)) # 바이러스 

# 벽을 세우는 코드
length = len(wall)
for i in range(length):
    for j in range(i):
        for k in range(j):
            board[wall[i][0]][wall[i][1]] = 1
            board[wall[j][0]][wall[j][1]] = 1
            board[wall[k][0]][wall[k][1]] = 1
            
            res = max(res, func())
            
            board[wall[i][0]][wall[i][1]] = 0
            board[wall[j][0]][wall[j][1]] = 0
            board[wall[k][0]][wall[k][1]] = 0
            
print(res)

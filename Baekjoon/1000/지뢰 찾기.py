# 지뢰 찾기.py 1996
# 지뢰가 있는 주변의 상,하,좌,우, 4개의 대각선 총 8개를 카운트한다

n = int(input())
board = list(input().rstrip() for _ in range(n))
ans = [[0] * n for _ in range(n)]
dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

for i in range(n):
    for j in range(n):
        if board[i][j].isdigit():

            for dir in range(0, 8):
                nx = i + dx[dir]
                ny = j + dy[dir]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                ans[nx][ny] += int(board[i][j])



for i in range(n):
    for j in range(n):
        if board[i][j].isdigit():
            print('*', end='')
        elif ans[i][j] >= 10:
            print('M', end='')
        else:
            print(ans[i][j], end='')
    print()

# 쿠키의 신체 측정.py 20125
# 머리를 먼저 찾고, 바로 밑의 심장 위치를 기준으로 팔, 허리, 다리를 dfs로 탐색하여 길이를 구했다
# 이때 다리가 관건인데 허리의 좌표를 따로 구하지 않고 심장의 좌표를 이용하여 다리의 시작점을 구했다

import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]


def dfs(dirX, dirY, cnt, x, y):
  nx = x + dirX
  ny = y + dirY

  if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] != '*': return cnt

  return dfs(dirX, dirY, cnt + 1, nx, ny)


def find_heart():
  for i in range(n):
    for j in range(n):
      if board[i][j] == '*':
        heart_x, heart_y = i + 1, j
        return heart_x, heart_y


heart_x, heart_y = find_heart()

left_arm = dfs(0, -1, 0, heart_x, heart_y) # x방향, y방향, 개수, x, y
right_arm = dfs(0, 1, 0, heart_x, heart_y)
waist = dfs(1, 0, 0, heart_x, heart_y)
left_leg = dfs(1, 0, 0, heart_x + waist, heart_y - 1)
right_leg = dfs(1, 0, 0, heart_x + waist, heart_y + 1)

print(heart_x + 1, heart_y + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)


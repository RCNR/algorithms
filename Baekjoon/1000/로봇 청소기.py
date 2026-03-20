# 로봇 청소기.py 14503
# 1. 현재 위치 청소
# 2. 주변 확인한다 == 회전해서 본다
# 3. 전진할 곳 좌표를 확인한다
# 4. 0이면 전진한다(위치 값 갱신한다)
# 5. 갈 곳이 없으면 후진한다(보는 방향은 그대로, 후진할 좌표 확인한다)
# 6. 후진할 곳이 벽이면 종료한다

# 0 북, 1 동, 2 남, 3 서

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

# 반시계 방향 90도 회전
def turn_left(dir):
  return (dir-1) % 4

while True:
  # 청소
  if board[r][c] == 0:
    board[r][c] = 123
    cnt += 1
  
  move = False

  # 주변 확인 + 회전
  for _ in range(4):
    d = turn_left(d) # 회전한다
    nx = r + dx[d] # 전진할 좌표를 확인한다
    ny = c + dy[d]

    if board[nx][ny] == 0: # 0이면 전진한다
      r, c = nx, ny # 위치 값 갱신한다
      move = True
      break
  
  if move: continue

  # 후진 (보는 방향 d는 그대로)
  back_dir = (d + 2) % 4 # 0<->2, 1<->3
  backX = r + dx[back_dir] # 후진할 좌표 확인한다
  backY = c + dy[back_dir]

  if board[backX][backY] == 1: # 벽이면 종료
    break
  
  r, c = backX, backY # 후진 좌표 갱신

print(cnt)

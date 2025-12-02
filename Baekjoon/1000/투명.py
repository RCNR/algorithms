# 투명 1531
# 겹치는 숫자세고 그게 m을 넘어가는지 확인

import sys
input = sys.stdin.readline

board = [[0] * 101 for _ in range(101)]

n, m = map(int, input().split())

cnt = 0

for _ in range(n):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(x2, x1-1, -1):
    for j in range(y2, y1-1, -1):
      board[i][j] += 1


for i in range(1, 101):
  for j in range(1, 101):
    if board[i][j] > m:
      cnt += 1



print(cnt)
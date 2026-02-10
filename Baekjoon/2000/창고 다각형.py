# 창고 다각형.py 2304
# 가장 큰 막대기를 기준으로 왼쪽, 오른쪽으로 나누어 생각
# 이때 높이가 같은 경우를 고려하여 왼쪽, 오른쪽 나눌 때 등호를 적절히 사용
# -> 높이가 같은 경우 중복 문제가 생긴다 그래서 위에서 등호를 했으니 한쪽에서는 제외한다.

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

board.sort()

# 왼쪽
res1 = 0
Q1 = deque()
for li in board:
  if len(Q1) != 0:
    if Q1[0][1] <= li[1]:
      res1 += ((li[0] - Q1[0][0]) * Q1[0][1])
      Q1.popleft()
    else:
      continue
  Q1.append(li)
  # print(Q1)

res2 = 0
Q2 = deque()
for i in range(n-1, -1, -1):
  li = board[i]
  if len(Q2) != 0:
    if Q2[0][1] < li[1]: # 높이가 같은 경우 중복 문제가 생긴다 그래서 위에서 등호를 했으니 여기서는 빼줘야한다
      res2 += ((Q2[0][0] - li[0]) * Q2[0][1])
      Q2.popleft()
    else: continue
  Q2.append(li)
  # print(Q2)
# print(res1, res2)
print(res1 + res2 + Q2[0][1])


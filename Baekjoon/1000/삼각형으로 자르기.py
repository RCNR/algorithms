# 삼각형으로 자르기.py 1198
# 문제 조건을 따라가다가 근본적인 것을 알 수 있는 문제
# 거기에 세 점을 이용한 삼각형 넓이 구하기 - 신발끈 공식

import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def func(x1, y1, x2, y2, x3, y3):
  ret = abs((x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1))
  return ret / 2

res = -1

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      x1, y1 = board[i][0], board[i][1]
      x2, y2 = board[j][0], board[j][1]
      x3, y3 = board[k][0], board[k][1]
      res = max(res, func(x1, y1, x2, y2, x3, y3))
print(res)
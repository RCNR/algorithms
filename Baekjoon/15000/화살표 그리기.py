# 화살표 그리기.py 15970
# 같은 색깔의 점들끼리 화살표를 그릴 때, 모든 점에서 화살표의 길이의 합의 최솟값을 구하는 문제
# 각 색깔별로 점들을 모은 뒤, 정렬하여 인접한 점들과의 거리 중 최솟값을 더함
# 첫번째와, 마지막번째만 한쪽 점과의 거리만 더함

import sys
from collections import defaultdict
input = sys.stdin.readline

board = defaultdict(list)

n = int(input())
for _ in range(n):
  num, color = map(int, input().split())
  board[color].append(num)


def func(l):
  res = 0
  for i in range(len(l)):
    if i == 0:
      res += abs(l[i] - l[i+1])
    
    elif i == len(l) - 1:
      res += abs(l[i] - l[i-1])
    
    else:
      res += min(abs(l[i] - l[i-1]), abs(l[i] - l[i+1]))
  
  return res


total = 0
for color in board:
  a = sorted(board[color])
  total += func(a)

print(total)
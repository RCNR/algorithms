# 이진 검색 트리.py 5639
# 이진 검색 트리의 전위 순회 결과가 주어졌을 때, 후위 순회 결과를 구하는 문제
# 전위 순회 결과를 이용해 이진 검색 트리를 구성한 뒤 후위 순회 결과를 출력
# 루트를 기준으로 왼쪽/오른쪽 서브트리를 나눈다 -> 재귀적으로 반복

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

board = []
for l in sys.stdin:
  board.append(int(l.strip()))

res = []

def func(st, en):
  if st >= en: return

  rt = board[st]
  idx = st + 1

  while idx < en and board[idx] < rt:
    idx += 1
  
  # 왼오부
  func(st + 1, idx)

  func(idx, en)

  print(rt)

func(0, len(board))


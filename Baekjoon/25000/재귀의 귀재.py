# 재귀의 귀재 25501

import sys
input = sys.stdin.readline
n = int(input())

board = list(input().rstrip() for _ in range(n))


def func(palin_str, st, en):
  global cnt
  cnt += 1
  if st >= en: return 1
  elif palin_str[st] != palin_str[en]: return 0
  else: return func(palin_str, st + 1, en - 1)

for string in board:
  st = 0
  en = len(string) - 1
  cnt = 0
  res = func(string, st, en)
  print(res, cnt)
  
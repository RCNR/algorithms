# 자두나무 2240
# dp를 이용해 움직임 횟수에 따른 각 초에 받을 수 있는 개수 구하기

import sys
input = sys.stdin.readline

# i번 움직였을 때, j초에 받을 수 있는 최대 사과 개수

n, m = map(int, input().split())
board = [0] +  list(int(input()) for _ in range(n))

dp = [[0] * (n+3) for _ in range(m+3)]

for i in range(1, n+1):
  if board[i] == 1:
    dp[0][i] += dp[0][i-1] + 1
  else:
    dp[0][i] += dp[0][i-1]

for i in range(1, m+1):
  for j in range(1, n+1):

    dp[i][j] = max(dp[i-1][j-1], dp[i][j-1])
    
    if i % 2 == 1: # 현재 2번 나무인 경우
      if board[j] == 2: dp[i][j] += 1

    else: # 현재 1번 나무인 경우
      if board[j] == 1: dp[i][j] += 1

res = -1
for d in dp:
  res = max(res, max(d))

print(res)
# 양팔저울 2629
# 추를 가지고 특정 weight를 만들기
# 무게는 추를 아예 놓지 않을 때, 구슬과 같은 방향에 놓을 때, 구슬의 반대 방향에 놓을 때에 따라 무게가 형성된다.
# 어떤 상태(무게)를 만들려면 특정 상태(이전 무게)를 기반으로 만들어진다.

import sys
input = sys.stdin.readline

n = int(input())
Mr_chu = list(map(int, input().split()))

m = int(input())
marble = list(map(int, input().split()))

dp = [[0] * 50000 for _ in range(n+2)]

Mr_chu.insert(0, 0)
marble.insert(0, 0)

for i in range(0, n+1):
  dp[i][0] = 1

for i in range(1, n+1):
  for j in range(1, 40002):
    dp[i][j] = max(dp[i][j], dp[i-1][j]) # 추를 추가 하지 않은 경우
    dp[i][j] = max(dp[i][j], dp[i-1][j + Mr_chu[i]]) # 추를 구슬과 같은 방향에 추가한 경우
    dp[i][j] = max(dp[i][j], dp[i-1][abs(j - Mr_chu[i])]) # 추를 구슬 반대 방향에 추가한 경우

for i in range(1, m+1):
  if dp[n][marble[i]] == 1: print('Y', end=' ')
  else: print('N', end=' ')
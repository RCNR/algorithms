# LCS 2.py 9252
# LCS의 길이 뿐만 아니라 실제 문자열도 출력하기
# DP 테이블을 채운 후 역추적 -> 역추적: LCS 문자열 채우기

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

n, m = len(s1), len(s2)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]


for i in range(1, n+1):
  for j in range(1, m+1):
    if s1[i-1] == s2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
      # res.append((s1[i-1]))
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = n, m
res = []

while i > 0 and j > 0:
  '''
  현재 위치에서 두 문자가 같다면
  대각선 위로 이동
  '''
  '''
  다르다면
  i,j를 채웠던 곳으로 이동 -> 현재 값과 같은 곳으로 이동
  '''
  if s1[i-1] == s2[j-1]:
    res.append(s1[i-1])
    i -= 1
    j -= 1
  
  elif dp[i][j] == dp[i-1][j]:
    i = i-1
  elif dp[i][j] == dp[i][j-1]:
    j = j-1

if len(res):
  print(len(res))
  print(''.join(reversed(res)))
else:
  print(len(res))
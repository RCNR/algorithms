# 학생 번호 1235

# 완전 탐색과 set을 이용해 학생들의 번호가 몇 개가 겹치는지 확인
# 슬라이싱을 이용해 문자열의 뒤부터(길이1) +1 씩 더하여 맨 앞까지 갈 수 있도록 하였다
# 이때 입력 조건 n의 개수를 만족하게 되면 그게 문제에서 말하는 가장 짧은 k가 된다

import sys
input = sys.stdin.readline

n = int(input())
board = list(input().rstrip() for _ in range(n))

length = len(board[0])

cnt = 1

for i in range(length):

  res = set()
  for j in range(n):
    res.add(board[j][-cnt:])
  
  if len(res) == n:
    print(cnt)
    exit()
  cnt += 1

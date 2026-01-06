# 수리공 항승.py 1449
# 테이프로 물이 샌 곳을 막는 문제
# 정렬하고 앞에서부터 테이프 길이만큼 막기
# 테이프는 자를 수 없음 -> 이 부분을 주의

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = list(map(int, input().split()))

board.sort()

cnt = 0
i = 0
loc = 0.0

for i in range(N):
  if board[i] > loc:
    loc = board[i] + L - 0.5
    cnt += 1

print(cnt)
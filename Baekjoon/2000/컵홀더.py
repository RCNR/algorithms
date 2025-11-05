# 2810 컵홀더
# S 양옆에는 컵홀더가 있고, LL 양옆에 컵홀더가 있다
# LL은 공간을 2개 차지하기에 LL을 중점적으로 봤다.
# S 여러개만 있거나, S여러개 + LL 만 있으면 상관없다.
# 하지만 LL이 2개 이상 있으면 2개의 공간을 차지하는 게 원인이 되어 반드시 컵홀더를 차지하지 못하는 인원이 생긴다.
# 차지하지 못하는 인원은 "LL의 개수 - 1" 만큼이다
# LL 개수는 LL이 하나이지만 L만 따로 카운트 해주고, 나누기 2를 해주었다.

n = int(input())
board = input().rstrip()

cnt = 0
for c in board:
  if c == 'L': cnt += 1

if cnt == 2 or cnt == 0: # LL 및 S만 있거나, 오로지 S만 있는 경우
  print(len(board))
else:
  print(len(board) - (cnt // 2 - 1)) ## LL이 2개 이상인 경우

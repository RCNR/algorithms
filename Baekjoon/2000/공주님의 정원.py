# 2457
# 그리디 문제 - 어떤 방식으로 해야할지 아직 잘 모르겠음
import sys
input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n):
    data = list(map(int, input().split()))
    board.append([data[0]*100 + data[1] , data[2]*100 + data[3]])

board.sort()

d_day = 0 # 꽃 지는 날
long_flower = 301 # 날짜 비교해야함

cnt = 0

while board:
    if d_day >= 1201 or long_flower < board[0][0]: break

    for _ in range(len(board)):
        if board[0][0] <= long_flower:
            d_day = board[0][1]
    



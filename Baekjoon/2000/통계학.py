# 2108
import sys
import bisect
import math
upper_bound = bisect.bisect_right
lower_bound = bisect.bisect_left
input = sys.stdin.readline


n = int(input())
board = [int(input()) for _ in range(n)]

board.sort()
sum = 0

for num in board:
    sum += num

# print()

print(round(sum / len(board)))
print(board[len(board) // 2])

cnt = 0 # 최빈값의 개수
ans = board[0] # 최빈값, 최빈값이 여러 개라면 그 중 2번째 놈, 1개 인 경우를 고려해 초기값을 첫번째 값으로 잡는다
is_it_2 = 0
i = 0
while i < n:
    cnt_num = upper_bound(board, board[i]) - lower_bound(board, board[i])
    
    if cnt_num > cnt:
        is_it_2 = 0 # 새로 구한 cnt_num의 최빈값이 더 크면 is_it_2 초기화
        ans = board[i] # -1 0 0 인 경우 고려해야함
    
    if cnt_num == cnt and is_it_2 == 0:
        is_it_2 = 1
        ans = board[i]
    
    cnt = max(cnt, cnt_num)

    i += cnt_num

print(ans)
print(board[n-1] - board[0])
# print(upper_bound(board, 2))
# print(lower_bound(board, 2))

# 1920 수 찾기
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input().rstrip())
board = list(map(int, input().split()))
m = int(input().rstrip())
check =  list(map(int, input().split()))

board.sort()

for num in check:
    val = bisect_left(board, num)
    if val < len(board) and board[val] == num:
        print(1)
    else:
        print(0)
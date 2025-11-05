# 18110
# 0 일 때 조심
import sys
import math
input = sys.stdin.readline


def check(num):
    if num - math.floor(num) >= 0.5:
        return math.floor(num) + 1
    else:
        return math.floor(num)

n = int(input())
board = [int(input().rstrip()) for _ in range(n) ]
board.sort()

num = check(n * 0.15)
new_num = n - (num*2)
new_board = []
for i in range(num, n-num):
    new_board.append(board[i])

if new_num != 0:
    res = sum(new_board) / new_num
else:
    res = 0

print(check(res))
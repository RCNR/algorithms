# 2903
n = int(input())

board = [0] * 17

board[0] = 4
num = 2
for i in range(1, 16):
    num = num * 2 - 1
    board[i] = num ** 2

print(board[n])
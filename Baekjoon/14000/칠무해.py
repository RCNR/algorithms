# 14729 - 칠무해
import sys
input = sys.stdin.readline

n = int(input())
board = [float(input()) for _ in range(n)]
board.sort()
for i in range(7):
    print(f'{board[i]:.3f}')

# 10994
import sys
sys.setrecursionlimit(10**6)

n = int(input())
board = [[' '] * 400 for _ in range(400)]  # n=100 일 때 397임

def func(n, x, y):
    length = 4*n-3
    if length == 1:
        board[x][y]='*'
        return

    for i in range(length):
        board[x][y+i] = '*'
        board[y+i][x] = '*'
        board[x+length-1][y+i] = '*'
        board[x+i][y+length-1] = '*'
    x += 2
    y += 2
    n -= 1
    func(n, x, y)
    
func(n, 0, 0)
for i in range((4*n)-3):
    for j in range(4*n - 3):
        print(board[i][j], end='')
    print()

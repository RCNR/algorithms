#2386
import sys
input = sys.stdin.readline

while(True):
    board = input().rstrip()
    if board[0] == '#': break
    check = board[0]
    cnt = 0
    new = board.upper()
    cnt += new.count(board[0].upper())
    print(f'{check} {cnt-1}')
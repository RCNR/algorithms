import sys
input = sys.stdin.readline

def func(c):
    if c == '-': return 0
    elif c == '\\': return 1
    elif c == '(' : return 2
    elif c == '@' : return 3
    elif c == '?' : return 4
    elif c == '>' : return 5
    elif c == '&' : return 6
    elif c == '%' : return 7
    elif c == '/' : return -1

while(True):
    board = input().rstrip()
    if board == '#': break
    res = 0
    num = len(board) - 1
    for i in board:
        res += (func(i) * (8**num))
        num -= 1
    print(res)



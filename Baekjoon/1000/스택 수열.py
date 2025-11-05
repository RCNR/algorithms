# 1874 스택 수열
import sys
input = sys.stdin.readline
n = int(input())
board = list(int(input()) for _ in range(n))

s = []
op = []
num = 1
for i in range(n):
    while num <= board[i]:
        s.append(num)
        op.append('+')
        num += 1

    if s[-1] != board[i]:
        print('NO')
        exit(0)
    
    s.pop()
    op.append('-')
        

print(*op, sep='\n')
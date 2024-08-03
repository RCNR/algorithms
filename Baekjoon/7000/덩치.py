import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(n):
        if board[i][0] < board[j][0] and board[i][1] < board[j][1]:
            cnt+=1
    print(cnt+1, end=' ')


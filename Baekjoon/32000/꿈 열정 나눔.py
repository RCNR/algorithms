# 32185
# 간단한 그리디 문제 단, 인원이 1명일 때 조심

import sys
input = sys.stdin.readline

board = []

n, m = map(int, input().split())

for i in range(n+1):
    v, p, s = map(int, input().split())
    sum = v + p + s
    board.append((sum, i))

board[1:] = sorted(board[1:], key=lambda x:-x[0])

cnt = 1
res = [0]
for i in range(1, len(board)):
    if(cnt == m): break

    if board[i][0] > board[0][0]: continue
    else:
        cnt += 1
        res.append(board[i][1])
    

print(*res)

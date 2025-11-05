#15565 슬라이딩 윈도우
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

board = list(map(int, input().split()))

if board.count(1) < k:
    print(-1)
    exit(0)
board.append(0)

s = 0
e = 0
cnt = 0
siz = 0
res = 0x3f3f3f3f

while e <= n:
    if cnt >= k:
        res = min(res, siz)
        siz -= 1
        if board[s] == 1: cnt -=1
        s += 1
        continue

    if e==n: break

    if board[e] == 1:
        cnt += 1
    siz+=1
    e += 1

print(res)
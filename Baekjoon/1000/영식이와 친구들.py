# 1592 - 단순 구현
N, M, L = map(int, input().split())

board = [0] * (N+2)
board[1] = 1

idx = 1
cnt = 0
while(True):
    if board[idx] == M:
        break

    if board[idx] % 2 == 1:
        idx += L
        if idx > N:
            idx -= N
        board[idx] += 1
    else:
        idx -= L
        if idx < 1:
            idx += N
        board[idx] += 1
    cnt += 1
print(cnt)





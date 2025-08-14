# 달팽이

num = int(input())
k = int(input())

board = [[0] * (num) for _ in range(num)]

cur_x = num // 2
cur_y = num // 2

res = []
idx = 2


def check(x, y):
    if board[x][y] == k:
        res.append(x)
        res.append(y)

board[cur_x][cur_y] = 1
check(cur_x, cur_y)



for i in range(1, num // 2 + 1):
    
    # ->
    cur_x -= 1
    for j in range(2 * i):
        board[cur_x][cur_y + j] = idx
        check(cur_x, cur_y + j)
        idx += 1
    cur_y += 2 * i - 1

    # down
    cur_x += 1
    for j in range(2 * i):
        board[cur_x + j][cur_y] = idx
        check(cur_x + j, cur_y)

        idx += 1
    cur_x += 2 * i - 1

    # <-
    cur_y -= 1
    for j in range(2 * i):
        board[cur_x][cur_y - j] = idx
        check(cur_x, cur_y - j)

        idx += 1
    cur_y -= 2 * i - 1

    # up
    cur_x -= 1
    for j in range(2 * i):
        board[cur_x - j][cur_y] = idx
        check(cur_x - j, cur_y)

        idx += 1
    cur_x -= 2 * i - 1

for i in range(num):
    for j in range(num):
        print(board[i][j], end = ' ')
    print()
    

print(res[0] + 1, res[1] + 1)



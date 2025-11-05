# 달팽이 1913

num = int(input())
k = int(input())

board = [[0] * num for _ in range(num)]

cur_x = num // 2
cur_y = num // 2
board[cur_x][cur_y] = 1

kx, ky = (cur_x, cur_y) if k == 1 else (-1, -1)

# 위, 오른쪽, 아래, 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1 ,0, -1]

cnt = 2 # 채우는 숫자
step = 1 # 현재 방향에서 몇 칸
dir = 0

while cnt <= num * num:
    for _ in range(2):
        for _ in range(step):
            
            if cnt > num * num: break

            cur_x += dx[dir]
            cur_y += dy[dir]
            board[cur_x][cur_y] = cnt

            if cnt == k: kx, ky = cur_x, cur_y

            cnt += 1
        dir = (dir + 1) % 4
    step += 1

for li in board:
    print(*li)

print(kx + 1, ky + 1)

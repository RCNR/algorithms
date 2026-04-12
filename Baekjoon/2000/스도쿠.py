# 스도쿠 2239
# 모든 경우 탐색 시 9^81이므로 불가능
# 가지치기를 통해 탐색 범위를 줄여야 함
# 1. 빈 칸에 1~9까지 숫자 넣어보기
# 2. 행, 열, 3x3에 이미 존재하는 숫자라면 가지치기
# 3. 존재하지 않는 숫자라면 다음 빈 칸으로 넘어가기
# 4. 모든 빈 칸을 채웠다면 스도쿠 완성, 출력 후 종료

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# row[i][num] - i번째 행에 num 있는지
# col[j][num] - j번째 행에 num 있는지
# square[k][num] - k번째 3x3에 num 있는지

board = [list(input().rstrip()) for _ in range(9)]
check = []

row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
square = [[False] * 10 for _ in range(9)]

def func(cnt):
    if cnt == len(check):
        for li in board:
            print("".join(li))

        sys.exit(0)
    
    x, y = check[cnt]
    k = (x // 3) * 3 + (y // 3)

    for number in range(1, 10):
        
        if not row[x][number] and not col[y][number] and not square[k][number]:
            row[x][number] = col[y][number] = square[k][number] = True
            board[x][y] = str(number)

            func(cnt + 1)
            row[x][number] = col[y][number] = square[k][number] = False
            board[x][y] = '0'


for i in range(9):
    for j in range(9):
        num = int(board[i][j])
        if num == 0: check.append((i, j))
        else:
            row[i][num] = True
            col[j][num] = True
            k = (i // 3) * 3 + j // 3
            square[k][num] = True


func(0)
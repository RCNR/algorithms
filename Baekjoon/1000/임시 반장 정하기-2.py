import sys
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

max_num = 0
max_index = 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j:
            for k in range(5):
                if board[i][k] == board[j][k]:
                    cnt += 1
                    break
    if cnt > max_num:
        max_num = cnt
        max_index = i + 1

print(max_index)
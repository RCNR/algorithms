# 2847
# 어떻게 하면 최소로 감소 시킬 수 있을지
# greedy적 생각 필요 -> 증가되는 순서여야 함 -> 역순(뒤에서부터)으로 생각해보자

n = int(input())

board = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-2, -1, -1):
    while board[i] >= board[i+1]:
        board[i] -= 1
        cnt += 1

print(cnt)

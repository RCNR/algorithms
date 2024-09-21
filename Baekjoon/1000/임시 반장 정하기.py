import sys
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

hero = []

for i in range(n):
    isused = [0]*n
    cnt = 0
    for j in range(5):
        for k in range(n):
            if board[i][j] == board[k][j]:
                if isused[k] == 1:
                    continue
                else:
                    cnt += 1
                    isused[k] = 1
    hero.append((cnt-1, i+1))

hero.sort(key=lambda x: (-x[0], x[1]))
print(hero[0][1])
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [int(input()) for _ in range(n)]
check = [0] * (m+3)

for num in board:
    for j in range(num, m+1, num):
        check[j] = 1
print(sum(check))
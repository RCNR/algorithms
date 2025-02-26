# 피보나치 수 6
# 행렬을 이용한 피보나치 계산 logN
mod = 1000000007
matrix = [[1,1], [1,0]]
res = [[1,0], [0,1]]

def func(a, b):
    siz = len(a)
    board = [[0] * siz for _ in range(siz)]
    for i in range(siz):
        for j in range(siz):
            for k in range(siz):
                board[i][j] += a[i][k] * b[k][j]
            board[i][j] %= mod
    return board


n = int(input())

while n > 0:
    if n % 2 == 1:
        res = func(res, matrix)
    matrix = func(matrix, matrix)
    n = n // 2

print(res[0][1])
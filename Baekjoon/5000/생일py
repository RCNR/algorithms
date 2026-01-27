# 생일.py 5635
# 가장 나이가 적은, 많은 사람 각각 출력하기
# 람다 사용해 정렬하여 출력하기

import sys
input = sys.stdin.readline

n = int(input())
board = [input().rstrip().split(' ') for _ in range(n)]
board.sort(key = lambda x : (int(x[3]), int(x[2]), int(x[1])))


print(board[n-1][0])
print(board[0][0])
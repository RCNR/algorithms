# 11478
# set과 슬라이싱을 이용해 구하기
import sys
input = sys.stdin.readline

board = set()
n = input().rstrip()

for i in range(0, len(n)):
    for j in range(len(n)-1, i-1, -1):
        sub = n[i:j+1]
        board.add(sub)
print(len(board))
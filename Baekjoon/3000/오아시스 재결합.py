# 오아시스 재결합 3015
import sys
input = sys.stdin.readline

n = int(input())
board = [int(input()) for _ in range(n)]

s = []
res = 0

for i in range(n):
    num = board[i]
    num_cnt = 1

    while len(s) != 0 and s[-1][0] <= num:
        res += s[-1][1] # top 관련

        if s[-1][0] == num:
            num_cnt += s[-1][1]
        s.pop()

    if len(s) != 0:
        res += 1 # top pop하고 push 해서 생기는 1개의 쌍
    s.append([num, num_cnt])

print(res)

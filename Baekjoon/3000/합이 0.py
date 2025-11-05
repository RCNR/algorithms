# 3151 합이 0
# 크기가 작아 배열로도 O, 정석- 이분탐색
import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))

cnt = [0] * 40001
res = 0
MID = 20000

for i in range(n-1):
    for j in range(i+1, n):
        num = -board[i] - board[j]
        res += cnt[num]
    cnt[board[i]] += 1
print(res)

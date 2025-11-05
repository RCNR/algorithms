import sys
input = sys.stdin.readline

n, d, k = map(int, input().split())

board = list(map(int, input().split()))


max_num = -1
for num in board:
    max_num = max(max_num, num)

res = 0
cnt = 0
for _ in range(d):
    if res + max_num > k:
        cnt += 1
        res = 0
    
    res += max_num

print(cnt)


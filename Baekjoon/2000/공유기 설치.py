# 2110 공유기 설치
# 공유기 사이 거리가 X 일 때 공유기 몇 대 설치 가능한지
import sys
input = sys.stdin.readline

n, m = map(int ,input().split())
board = [int(input()) for _ in range(n)]
board.sort()

def func(mid):
    pre = board[0]
    cnt = 1 # 맨 앞에는 가져간다고 생각
    for i in range(1, n):
        if board[i] - pre >= mid:
            cnt += 1
            pre = board[i]
    return cnt

st = 0
en = board[n-1]
res = 0

while st <= en:
    mid = (st + en) // 2
    shareCount = func(mid)
    
    if shareCount >= m:
        res = mid
        st = mid + 1
    else:
        en = mid - 1

print(res)


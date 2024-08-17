# 1253
# 투 포인터로 품 -> 모든 인덱스 숫자 검사, st/en은 양쪽 끝으로 설정하고 하면 됨
# 조건이 여러개라서 상당히 까다로움
import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
board.sort()

cnt = 0

for i in range(n):
    st = 0
    en = n-1
    now = board[i]

    while st < en:
        if board[st] + board[en] > now:
            en -= 1
        if board[st] + board[en] == now:
            if st==en: break
            if board[st] == now and st==i: # -2 -2 -1 -1 0 : 4개
                st+=1
                continue
            if board[en] == now and en==i: 
                en-=1
                continue

            cnt += 1
            # print(f'st = {board[st]}, en = {board[en]}, now = {now}, i = {i}')
            break
        if board[st] + board[en] < now:
            st += 1
        
print(cnt)
# 5
# -1 0 1 2 3
# 정답 : 4
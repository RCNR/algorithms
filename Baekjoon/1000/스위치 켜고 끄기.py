# 남학생(1)은 부여받은 번호의 배수를 모두 바꾼다.
# 여학생(2)은 부여받은 번호를 기준으로 양 옆이 비대칭일 때까지 바꾼다.
# 남학생 구할 때 완탐
# 여학생 구할 때 투포인터

import sys
input = sys.stdin.readline

N = int(input())
board = [-1] + list(map(int, input().split()))
M = int(input())
cnt = 0

for _ in range(M):
    s, num = map(int, input().split())

    if s == 1:
        for i in range(num, N+1, num):
            board[i] = 1 - board[i]
    else:
        board[num] = 1 - board[num]
        st = num - 1
        en = num + 1
        while st >= 1 and en <= N:
            if board[st] == board[en]:
                board[st] = 1 - board[st]
                board[en] = 1 - board[en]
                st -= 1
                en += 1
            else:
                break
        

for i in range(1, N+1):
    print(board[i], end = ' ')
    if i % 20 == 0: print()

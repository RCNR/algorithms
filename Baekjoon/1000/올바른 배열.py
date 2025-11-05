# 1337 
# 정렬, 답은 0~4 사이라는 사실, 양 끝을 포인터로 잡고 5이상인지, 4이하인지 판단
# 4이하 라면 인덱스 값을 사용하여 그 구간에 몇개의 값이 들어가게 되는지 확인

import sys
input = sys.stdin.readline

n = int(input())
board = [int(input()) for _ in range(n)]
board.sort()

num = 4 # 정답이 0 ~ 4 사이

for i in range(len(board)):
    st = i
    end = n-1
    while st < end:
        if board[end] - board[st] >= 5:
            end -= 1
        else:
            num = min(num, 4-(end-st)) # 4 이하 인 경우
            st += 1
print(num)


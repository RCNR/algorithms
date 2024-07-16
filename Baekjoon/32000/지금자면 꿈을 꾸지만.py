# 32029
import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
board = list(map(int, input().split()))
board.sort()

max_cnt = -1

for i in range(0, A):
    sleep_time = B * i
    for j in range(len(board)+1): # 70 80 90 이 있다면 sleep_time은 * 70 * 80 * 90 * 중에서 하나 존재해야함. 여기서 j는 * 중 하나를 의미, *은 board의 길이보다 하나 더 많음

        cnt = 0
        change_time = sleep_time
        no_sleep = 0

        for k in range(j): # j-1까지 구하고 ==> 자지 않고 과제하는 시간
            if board[k] - no_sleep - A >= 0:
                cnt += 1
                no_sleep += A

        change_time += no_sleep
        
        for k in range(j, len(board)): # j부터 끝까지. 즉, sleep한 이후에 과제하는 부분을 구해준다
            if board[k] - change_time - (A-i) >= 0:
                cnt += 1
            change_time += (A - i)

        max_cnt = max(max_cnt, cnt)

print(max_cnt)

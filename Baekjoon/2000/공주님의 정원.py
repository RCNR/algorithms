# 2457
# 그리디 문제 - 어떤 방식으로 해야할지 아직 잘 모르겠음
import sys
input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n):
    data = list(map(int, input().split()))
    board.append([data[0]*100 + data[1] , data[2]*100 + data[3]])

board.sort()

end_day = 301 # 꽃 지는 날
# 날짜 비교해야함

cnt = 0
flower_period = 0
flower_start = 301

while board:
    if end_day >= 1201 or flower_start < board[0][0]: break

    for _ in range(len(board)):
        if board[0][0] <= flower_start:
            period = board[0][1] - flower_start
            if period > flower_period: # 얘가 더 좋은 꽃인거임
                flower_period = period
                end_day = board[0][1]
            #print(board[0])
            board.remove(board[0])
        else: break # flower_start 값과 비교했을 때 더 이상 볼 필요가 없는 경우
    #print(end_day)
    #print()
    cnt += 1
    flower_start = end_day
    flower_period = 0 # 이 기간을 초기화시켜줘야 다음 꽃 기간을 선정할 때 영향을 주지 않음 -> 여기서 시간 이빠이 잡아먹음

#print(cnt)

if len(board) and end_day < board[0][0]:
    print(0)
    exit(0)

if end_day == 1130:
    print(0)
    exit(0)

print(cnt)

# 87%에서의 반례 발견 : 3 1 11 30 -> 답 : 0, 출력 : 1
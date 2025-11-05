# 11000
import sys
import heapq
input = sys.stdin.readline

n = int(input())
board = [list(map(int ,input().split())) for _ in range(n)]

board.sort() # 강의 시작하는 순서로 정렬 -> 앞의 강의의 끝나는 시간과 다음 강의들의 시작 시간이 중요함

# 현재 강의의 끝나는 시간보다 다음 강의의 시작 시간(board[i][0])이 더 빠르면 새로운 강의실을 열어야함
# 그게 아니라면 그 강의실을 또 사용 가능
q = []
heapq.heappush(q, board[0][1]) # 시작값으로 맨 처음에 시작하는 강의의 종료 시간을 넣어줌

for i in range(1, n):
    if board[i][0] >= q[0]:
        heapq.heappop(q) # q맨 앞의 강의실을 이어서 사용할 수 있으므로 pop 해주고
    heapq.heappush(q, board[i][1]) # 이어서 사용하는 강의의 끝나는 시간을 q에 추가
print(len(q))
    

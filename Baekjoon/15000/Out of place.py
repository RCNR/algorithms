# Out of Place.py 15594
# 그리디스럽게 단순하게 생각한다.
# 정렬된 배열에서 하나의 원소만 위치가 다르다. 이로 인해 발생하는 swap 개수를 세야하는데, 정렬 배열과 뒤바뀐 배열의
# 인덱스마다 다른걸 카운트하고 최종적으로 -1을 해줘야한다. 마지막에 바뀌는 경우를 생각했을 때, +1 이 추가되기 때문에

import sys
input = sys.stdin.readline

n = int(input())
board = [int(input()) for _ in range(n)]
sorted_board = sorted(board)
cnt = 0
for i in range(n):
    if board[i] != sorted_board[i]:
        cnt += 1

print(0 if cnt == 0 else cnt - 1)

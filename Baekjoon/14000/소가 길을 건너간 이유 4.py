# 소가 길을 건너간 이유 4 14464
# C 마리 닭, T 초에만 소를 도와준다.
# 소는 총 N마리, 소는 A ~ B 초 사이에 길을 건너야 한다.
# 따라서 T는 A, B 사이에 있어야 한다
# C, N 20000 이하이다.
# 닭을 이용해 소가 최대한 많이 건너야 한다.

# "빠른 초에 출발하는 닭을 뽑고, A ~ B가 작은 소를 뽑아 닭 시간에 소가 나갈 수 있는지 비교하면 되지 않나?" 라는 생각
# 소의 A를 기준으로 한다면(시작 기준) -> 예제를 이용해 0, 3이 아닌 0, 100인 경우(답:4) 답이 3이 나오므로 불가능하다.
# 소의 B를 기준으로 한다면(끝 기준) -> 마찬가지로 불가능하다.
# 시작과 끝의 짬뽐이라고 생각
# 최대한 닭을 많이 이용하기 위해서는 소의 이동이 가능한 시간에서 시작보다는 끝을 중점적으로 봐야겠다고 생각
# => 이에, 소의 B를 기준으로 정렬 -> B가 같다면 A 기준으로 정렬
# 정렬된 소들의 첫 번째부터 루프를 돌면서 이용할 수 있는 닭의 위치를 bisect을 이용해 찾고 소가 닭을 이용할 수 있는지 확인한다.

import sys
from heapq import *
import bisect
input = sys.stdin.readline

C, N = map(int, input().split())
board = list(int(input()) for _ in range(C))
cow = [list(map(int, input().split())) for _ in range(N)]

board.sort()
cow.sort(key=lambda x: (x[1], x[0])) # B기준 오름차순, A기준 오름차순

cnt = 0
for num in cow: # 소 개수 만큼 루프 
    cur = bisect.bisect_left(board, num[0]) # 닭의 시간에 있어서 닭 시간보다 작은 소의 최소 출발 시간
    if cur != len(board) and  board[cur] <= num[1]: # 모든 닭 보다 출발 시간이 이르고, 닭 시간이 소의 최대 출발보다 일러야함
        cnt += 1
        board.pop(cur) # 닭을 사용했으니 인덱스 cur의 위치에 있는 닭을 뺀다.

print(cnt)


# 우선순위 큐를 이용한 두번 째 방법
import sys
from heapq import *
input = sys.stdin.readline

C, N = map(int, input().split())
chicken = list(int(input()) for _ in range(C))
cow = [list(map(int, input().split())) for _ in range(N)]

chicken.sort()
cow.sort()

idx = 0
res = 0
pq = []

for num in chicken:
    while idx < N and cow[idx][0] <= num:
        heappush(pq, cow[idx][1]) # 소의 끝을 우선순위에 넣어줌
        idx += 1
    
    while len(pq) != 0 and pq[0] < num: # 소의 끝이 닭보다 빠른 경우 불가능
        heappop(pq)
    
    if len(pq) != 0:
        res += 1
        heappop(pq)

print(res)
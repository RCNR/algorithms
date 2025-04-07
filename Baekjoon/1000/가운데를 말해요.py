# 가운데를 말해요 1655
# N은 최대 100,000 이고 0.1초 빠르게 끝나야함 
# 수의 중간값을 말한다
# i번째 기준으로 총 수의 개수가 짝수라면 중간 2개 중 작은 값 말한다
# 어떻게 그때마다 중간 수를 말할 수 있을까?
# 1. 그냥 매번 정렬하고 중간 값 구하기 -> N * NlogN -> 시간 초과
# 2. 힙을 사용해 루프 돌 때마다 중간값을 출력하면 되지 않나 -> heap은 루트 값만 제대로 된 값을 가져올 수 있음
# 3. 최소 힙, 최대 힙 나눠서 각 힙마다의 루트를 보며 중간 확인
import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
board = [int(input()) for _ in range(n)]

pq_min = []
pq_max = []

for num in board:
    
    if len(pq_max) == 0 or num <= -pq_max[0]:
        heappush(pq_max, -num)
    else:
        heappush(pq_min, num)
    
    if len(pq_min) > len(pq_max): # pq_max가 개수가 더 적은 경우 pq_min에서 값을 가져옴
        heappush(pq_max, -heappop(pq_min))
    
    # pq_min의 개수가 더 적은 경우 pq_max에서 값을 가져오는데 막 가져오면 안됨
    elif len(pq_min) + 1 < len(pq_max): 
        heappush(pq_min, -heappop(pq_max))
    print(-pq_max[0])
    # print(f'max = {-pq_max[0]}')
# print(pq_min)
# print(pq_max)


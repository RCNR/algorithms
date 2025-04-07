# 파일 합치기 3 13975
# 여러 개의 파일이 있고 이를 하나의 파일로 구성해야한다
# 각 비용은 파일들을 합치는 비용이다
# 최종 하나의 파일로 만드는 비용을 최소화 -> 현재 파일들 중 가장 작은 값 2개를 꺼내어 합해야 최소화 가능 -> minHeap
# 가장 작은 값들 2개를 꺼내 결과를 넣어주고 2개의 합을 다시 넣어준다

import sys
from heapq import *
input = sys.stdin.readline

def func():
    res = 0
    while len(pq) > 1:
        num1 = heappop(pq)
        num2 = heappop(pq)
        res += num1 + num2
        heappush(pq, num1 + num2)
    print(res)

n = int(input())
for _ in range(n):
    num = int(input())
    pq = list(map(int ,input().split()))
    heapify(pq)
    func()
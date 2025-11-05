# 22254 공정 컨설턴트 호석
# i번 선물은 사용 시간이 가장 적은 공정 라인 중 하나에 배정됨
# 비용을 아끼기 위해 공정 라인 개수 최소화

# 선물을 라인에 넣을 때마다 가장 적은 공정 라인에 넣는다 -> 우선순위 큐
# 어떻게 풀지는 확인됨 필요한 공정 라인 개수는 어떻게 확인해야하나
# 1개 일 때, 2개 일 때, 3개 일 때... -> 예제는 1개 일 때 F, 2개 일 때 F, 3개 일 때는 됨 T, 4개 일 때 T, 5개 일 때 T, ...
# -> 공정 라인 개수 늘어나면 모든 선물 만드는 시간은 줄어듬
# => FFFFTTTT (파라메트릭) -> T중의 최솟값 반환 -> high 반환

# 개수가 k 일 때 우선순위 큐에서 top에 있는 것에 시간을 더해줌 - 시간 넘으면 아닌거

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(map(int, input().split()))


def func(cur):
    pq = [0] * cur
    
    # 공정 라인 개수가 cur일 때, 시간
    time = 0 

    for num in board:
        new_time = heapq.heappop(pq) + num
        heapq.heappush(pq, new_time)
        time = max(time, new_time)
    
    return time <= m



low = 0
high = 100000

while low + 1 < high:
    mid = (low + high) // 2

    # func(mid)가 시간 안에 만들 수 있으면
    if func(mid):
        high = mid
    else:
        low = mid

print(high)
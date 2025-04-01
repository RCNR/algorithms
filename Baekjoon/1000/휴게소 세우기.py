# 1477 휴게소 세우기
# M 개 지을 때 휴게소 간 거리의 최댓값의 최솟값 -> 거리의 최댓값을 k로 할 때 M개 이하의 휴게소가 추가로 필요한가
import sys
input = sys.stdin.readline

N, M, L = list(map(int, input().split()))
board = list(map(int, input().split()))
board.append(0)
board.append(L)
board.sort()


def func(k):
    cnt = 0

    for i in range(1, N+2):
        dist = board[i] - board[i-1]
        cnt += dist // k
    
        if dist % k == 0:
            cnt -= 1
    
    return cnt <= M
    # 설치하는 휴게소가 M 이하인가?
    # M 이하이면 high를 mid로 가야함 -> 설치할 수 있는 휴게소 개수가 늘어남


# 1 ~ L 
low = 1
high = L 


while low  < high:
    mid = (low + high) // 2

    res = func(mid)
    if res:
        # 정답 [low, mid] 존재
        high = mid
    else:
        # 정답 [mid+1, high] 존재
        low = mid + 1

print(low)
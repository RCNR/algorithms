# 반전 요세푸스.py 20301
# deque의 rotate함수를 사용
# rotate 함수는 C로 최적화 되어있다고 한다 -> 매우 빠르다
import sys
from collections import deque
input = sys.stdin.readline

N, K, M = map(int, input().split())
Q = deque(range(1, N+1))

is_right = True
cnt = 0
kill = 0
while Q:
    if is_right:
        Q.rotate(-(K - 1))
        print(Q.popleft())
    
    else:
        Q.rotate(K - 1)
        print(Q.pop())
        
    kill += 1
    if kill == M:
        is_right = not is_right
        kill = 0




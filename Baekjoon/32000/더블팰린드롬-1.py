# 32357
# 첫 번째 방식과 달리 메모리, 시간 측면에서 더 효율적
# 슬라이싱 기법을 이용하자
import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
for _ in range(n):
    res = input().rstrip()
    if res == res[::-1]:
        cnt += 1

print(cnt * (cnt-1))

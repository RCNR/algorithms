# 가장 긴 증가하는 부분 수열 2.py 12015
# 이분탐색을 이용한 가장 긴 증가하는 부분 수열 O(N log N)
# LIS 문제이고, n^2 풀이로는 시간초과
# 오름차순 이기에 특정 숫자 X가 들어갈 위치를 찾아야 한다
# 유지하고 있는 배열은 무조건 오름차순으로 유지된다는 생각

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))

arr = []

for num in board:
    idx = bisect_left(arr, num)
    
    if idx == len(arr):
        arr.append(num)
    else:
        arr[idx] = num

print(len(arr))
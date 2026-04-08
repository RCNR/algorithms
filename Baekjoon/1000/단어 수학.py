# 단어 수학 1339
# 각 알파벳이 0~9 사이의 숫자 하나로 바뀌었을 때, 그 수들의 합이 최대가 되도록 하는 프로그램
# 처음에는 길이 비교를 통해 더 큰쪽에 큰 수 부여, 같아 지는 지점에아무거나 먼저 큰 수 부여 방식 생각
# 즉 heap 구조를 생각함
# 하지만 알파벳이 여러 번 등장해 누적되는 가중치 고려 못함 ex) 100의 자리에 1번 등장하는 것보다, 10의 자리에 12번 등장하는 게 전체 합에 더 큰 영향 줌
# 글자 길이나 위치에 따라 매번 숫자 할당이 아닌, 각 알파벳이 결과값에 기여하는 총 가중치 먼저 계산 후 숫자(9~0) 할당

import sys
input = sys.stdin.readline
from heapq import *
from collections import defaultdict
n = int(input())

board = list(input().rstrip() for _ in range(n))


num = 9
m = defaultdict(int)

for word in board:
  length = len(word)
  for idx, char in enumerate(word):

    p = 10**(length - idx - 1)

    if char in m:
      m[char] += p
    else:
      m[char] = p

weights = sorted(m.values(), key=lambda x : -x)
res = 0

for weight in weights:
  res += weight * num
  num -= 1

print(res)


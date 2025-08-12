# 파일 정리.py 20291

import sys
from collections import defaultdict 
input = sys.stdin.readline

n = int(input())
board = [input().rstrip() for _ in range(n)]
res = defaultdict(int)

for s in board:
    idx = s.find('.')
    name = s[idx+1:]
    res[name] += 1

for a, b in sorted(res.items()):
    print(a,b)


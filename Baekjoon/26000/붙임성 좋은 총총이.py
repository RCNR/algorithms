# 붙임성 좋은 총총이.py 26069
# set 자료구조를 이용하여 총총이와 붙임성 좋은 친구들을 저장해서 set 길이 구하기

import sys
input = sys.stdin.readline

n = int(input())
check = set()
check.add('ChongChong')
for i in range(n):
  a, b = map(str, input().split())
  
  if a in check or b in check:
    check.add(a)
    check.add(b)

print(len(check))
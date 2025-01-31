# 16165 걸그룹 마스터 준석이
# 해시 -> 딕셔너리 사용
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ary = {}
for _ in range(n):
  team = input().rstrip()
  num = int(input())
  member = list(input().rstrip() for _ in range(num))
  for i in range(len(member)):
    ary[member[i]] = team
  ary[team] = member

for _ in range(m):
  check = input().rstrip()
  num = int(input())
  if num == 1:
    print(ary[check])
  else:
    for member in sorted(ary[check]):
      print(member)

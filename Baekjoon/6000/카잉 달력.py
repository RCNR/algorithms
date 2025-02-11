# 6064 카잉 달력

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


# def func(x, y, resX, resY, cnt):
  
#   if x == resX and y == resY:
#     return cnt
  
#   if x > M:
#     x = 1
#   if y > N:
#     y = 1

#   if x==M and y==N:
#     return -1

#   cnt+=1
#   return func(x+1, y+1, resX, resY, cnt)



# for ary in board:
#   M = ary[0]
#   N = ary[1]
#   cnt = 1
#   result = func(1, 1, ary[2], ary[3], cnt)
#   print(result)
# 위에 처럼 하면 MN = 40000 * 40000 => 메모리 초과

def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return int(a * b / gcd(a, b))

def func(x, y):
  res = lcm(M, N)
  # print(res)
  if x == y: return x
  if x == M and y == N: return res

  for i in range(x, res, M):
    # x+M 배수 -> N으로 나눠서 y 되면 됨
    # if i%N == y%N:

    # 중국인의 나머지 정리
    if (i-y) % N == 0:
      return i
    
  return -1

for ary in board:
  M = ary[0]
  N = ary[1]
  x = ary[2]
  y = ary[3]
  print(func(x, y))
  

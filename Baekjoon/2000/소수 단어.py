# 소수 단어.py 2153
# 단어의 각 글자에 해당하는 수의 합이 소수인지 판별하기
# 소수 판별은 제곱근까지 확인

import math
s = input().rstrip()

res = 0

def is_prime():
  for i in range(2, int(math.sqrt(res)) + 1):
    if res % i == 0:
      print('It is not a prime word.')
      return
  
  print("It is a prime word.")

for c in s:
  if 'a' <= c <= 'z':
    res += ord(c) - ord('a') + 1
  
  else:
    res += ord(c) - ord('A') + 27


is_prime()
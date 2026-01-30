# 반복수열.py 2331
# 주어진 수열에서 처음으로 반복되는 수가 나오기 전까지 나온 수들의 개수를 구하는 문제
# dict() 리스트 이용해서 풀이
# dict에는 value 값을 seq의 길이(=인덱스)로 사용하여 해당 수가 몇 번째에 나왔는지 저장

from collections import defaultdict

A, P = map(int, input().split())

res = defaultdict(int)
res[A] = 0 # value 값을 인덱스로
seq = [A]

while True:
  newA = str(seq[-1])
  nxt = 0
  for num in newA:
    nxt += int(num) ** P
  
  if nxt in res:
    print(res[nxt])
    break
  
  res[nxt] = len(seq)
  seq.append(nxt)




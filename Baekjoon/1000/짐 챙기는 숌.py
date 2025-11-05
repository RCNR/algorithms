# 짐 챙기는 숌 1817

n, m = map(int, input().split())
if n==0:
  print(0)
  exit()
book = list(map(int, input().split()))

cnt = 1
is_full = 0
for num in book:
  is_full += num
  if is_full > m:
    cnt += 1
    is_full = 0
    is_full += num


print(cnt)
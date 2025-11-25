# 선물.py 1166
# 정수 이분탐색이 아닌, 소수 이분탐색
# 길이가 X일때 만들 수 있는 선물 개수

N, L, W, H = map(int, input().split())

st = 0
en = max(L, W, H)

# 길이 x일 때, 만들 수 있는 개수

for _ in range(1000):
  mid = (st + en) / 2

  cnt = (L//mid) * (W//mid) * (H//mid) # 가능한 개수

  # print(cnt)
  if cnt < N:
    en = mid
  
  elif cnt >= N:
    st = mid

print(en)
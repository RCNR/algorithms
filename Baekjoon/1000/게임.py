# 게임.py 1072
# 게임을 T판 했을 때 확률의 값이 X를 넘어가는 최소의 Y판을 구하는 문제
# 새로운 판을 Y판 더 했을 때 (Y + 현재 이긴 판수) / (Y + 현재 판수) * 100 > X 가 되는 최소의 Y를 구하는 문제

x, y = map(int, input().split())

l = 0
h = int(1e9) + 1

win_percent = (y * 100) // x

if win_percent == 99 or win_percent == 100:
  print(-1)
  exit(0)

while l + 1 < h:
  mid = (l + h) // 2

  new_percent = ((y + mid) * 100) // (x + mid)
  # print(new_percent, win_percent)


  if new_percent > win_percent:
    h = mid 
  
  elif new_percent <= win_percent:
    l = mid 
  

print(h)

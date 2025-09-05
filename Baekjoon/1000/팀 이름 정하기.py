# 팀 이름 정하기.py 1296
s = input().rstrip()
n = int(input())

board = list(input().rstrip() for _ in range(n))
win = []

for name in board:
  new = name + s
  L = new.count('L')
  O = new.count('O')
  V = new.count('V')
  E = new.count('E')

  total = (L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)
  win.append([total % 100, name])

win.sort(key=lambda x: (-x[0], x[1]))

print(win[0][1])
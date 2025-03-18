import sys
input = sys.stdin.readline
n = int(input())

def func(c) :
  if len(ary) == 0:
      ary.append(c)
      return
  if ary[-1] == 'A':
    ary.pop()
    ary.append('K')
  elif ary[-1] == 'K':
    ary.pop()
    # ary.append('B')
    func(c)
    ary.append('A')
  elif ary[-1] == 'B':
    ary.append(c)

for _ in range(n):
  board = list(str(input().rstrip()) for _ in range(2))
  ary = []
  for i in range(len(board[1])):
    c = board[1][i]
    if len(ary) == 0:
      ary.append(c)
    else:
      if c == 'B':
        func(c)

      elif c == 'A':
        ary.append(c)

  print(''.join('AB' if x == 'K' else x for x in ary))

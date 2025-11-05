# 3613 Java vs C++
import sys
input = sys.stdin.readline
ary = input().rstrip()

check = [0] * 3
for char in ary:
  if char.islower(): check[0] += 1
  elif char.isupper(): check[1] += 1
  elif char == '_': check[2] += 1

if (check[0] and check[1] and check[2]) or (ary[0] == '_' or ary[len(ary)-1] == '_') or (ary[0].isupper()):
  # 대문자, 소문자, '_' 섞인 경우
  # 시작 또는 마지막이 '_' 인 경우
  # 첫 시작이 대문자인 경우
  print("Error!")
  exit(0)

for i in range(len(ary)):
  # '_' 가 연달아 있는 경우
  if ary[i] == '_':
    if ary[i-1] == '_' or ary[i+1] == '_':
      print("Error!")
      exit(0)

if check[0] and check[2]:
  board = ary.split('_')
  for i in range(1, len(board)):
    board[i] = board[i][0].upper() + board[i][1:]
  print(''.join(board))

elif check[0] and check[1]:
  res = []
  remember_last_uppercase_idx = 0
  for i in range(len(ary)):
    if ary[i].isupper():
      res.append(ary[remember_last_uppercase_idx:i])
      res.append('_')
      res.append(ary[i].lower())
      remember_last_uppercase_idx = i + 1
  res.append(ary[remember_last_uppercase_idx:])
  print(''.join(res))
else:
  print(ary)
  

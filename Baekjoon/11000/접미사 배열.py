# 11656
s = input().rstrip()

board = []

for i in range(len(s)):
    board.append(s[i:len(s)])

board.sort()
# print('\n'.join(board))
print(*board, sep='\n')

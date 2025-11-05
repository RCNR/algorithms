# 킹.py 1063
# 구현, 8방향 탐색. 기존 문제들과 달리 x, y 좌표를 조금 변형해야 했다.

import sys
input = sys.stdin.readline
king, stone, n = map(str, input().split())
kx = 8 - int(king[1])
ky = ord(king[0]) - ord('A')

sx = 8 - int(stone[1])
sy = ord(stone[0]) - ord('A')
n = int(n)
board = [input().rstrip() for _ in range(n)]



move = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (1, 0),
    'T' : (-1, 0),
    'RT' : (-1, 1),
    'LT' : (-1, -1),
    'RB' : (1, 1),
    'LB' : (1,-1)
}

def check(x, y):
    if x < 0 or x > 7 or y < 0 or y > 7: return 1
    return 0

for m in board:
    dx, dy = move[m]
    nx = kx + dx
    ny = ky + dy
    if check(nx, ny): continue
    if nx == sx and ny == sy:
        if check(sx + dx, sy + dy): continue
        sx += dx
        sy += dy
    
    kx, ky = nx, ny


print(''.join([chr(ky + ord('A')), str(8 - kx)]))
print(''.join([chr(sy + ord('A')), str(8 - sx)]))


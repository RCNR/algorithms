# 22351
import sys
input = sys.stdin.readline

n = input().rstrip()

board = [int(n[0]), int(n[:2]), int(n[:3])]

for i in board:
    end_num = i
    new_num = ''
    
    while len(new_num) < len(n):
        new_num += str(end_num)

        if new_num == n:
            print(f'{i} {end_num}')
            exit(0)
        end_num += 1

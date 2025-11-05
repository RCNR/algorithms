# 3058
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
        board = list(map(int, input().split()))
        small = 200
        sum = 0
        for num in board:
            if num%2 == 0:
                sum += num
                small = min(small, num)
    
        print(sum, small)

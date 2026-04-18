# 칸토어 집합 4779
# 3^n 문자열 만들고, 3^n 문자열에서 가운데 3^(n-1) 문자열을 공백으로 바꿔주는 것을 n번 반복
# 중앙 공백 채우고, 왼쪽과 오른쪽 공백 채우는 재귀함수 만들기

import sys
input = sys.stdin.readline

def func(st, siz, ary):
    
    if siz == 1: return

    new_siz = siz // 3

    for i in range(st + new_siz, st + new_siz * 2):
        ary[i] = ' '
    
    func(st, new_siz, ary)

    func(st + new_siz * 2, new_siz, ary)

for n in sys.stdin:

    num = int(n)
    size = 3 ** num

    board = ['-'] * size
    func(0, size, board)

    print(''.join(board))
# 1759 암호 만들기
# 모음 1개, 자음 2개 이상을 포함하는 길이 n만들기
# 순서가 필요하니 정렬을 하고 앞에서부터 조합을 구한다 -> 재귀로 구현


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = list(map(str, input().split()))

result = [''] * 20

def check(vowel):
    return vowel == 'a' or vowel ==  'e'  or vowel == 'i' or vowel ==  'o' or vowel == 'u'

def func(num, start): # num은 선택 개수의 인덱스 값, start는 인덱스 값
    if num == n:
        cnt_vowel = 0 
        cnt_con = 0
        for i in range(n):
            if check(board[result[i]]): cnt_vowel += 1
            else: cnt_con += 1
    
        is_ok = False
        if cnt_vowel >= 1 and cnt_con >= 2: is_ok = True

        if is_ok:
            for i in range(n):
                print(board[result[i]], end='')
            print()
    
    for i in range(start, m):
        # result 배열에 인덱스 값들을 넣는다
        # -> 인덱스를 갖는 result 배열을 이용해 board 배열에서 result가 갖는 값이 모음인지 확인
        result[num] = i 
        func(num + 1, i + 1)

board.sort()
func(0, 0)

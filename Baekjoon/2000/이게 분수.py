# 이게 분수? 2863
# 4번 회전 하는 분수를 배열에 넣어 가장 큰 값의 인덱스를 구한다.


a, b = map(int, input().split())
c, d = map(int, input().split())


board = [a/c + b/d, c/d + a/b, d/b+ c/a, b/a + d/c]
print(board.index(max(board)))
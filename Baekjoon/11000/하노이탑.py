#11729
# n-1개 원판을 1(a) -> 2번(6-a-b) 기둥으로
# n번 원판을 1(a) -> 3번(b) 기둥으로
# n-1개 원판을 2(6-a-b) -> 3번(b) 기둥으로     => 원판이 n-1개일 때 원판을 옮길 수 있으면 n개 일 때도 옮길 수 있다

from sys import setrecursionlimit

setrecursionlimit(10**6)


def func(a, b, n): # (시작, 도착, n)
    global cnt
    if n==1:
        print(a, b)
        return
    func(a, 6-a-b, n-1)
    print(a, b)
    func(6-a-b, b, n-1)

n = int(input())

print((1<<n)-1)
func(1, 3, n)


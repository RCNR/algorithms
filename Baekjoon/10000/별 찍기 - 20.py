# 10995


n = int(input())

def check(m):
    global n
    if m%2 ==1:
        for _ in range(n):
            print('*', end='')
            print(' ', end='')
        print()

    else:
        for _ in range(n):
            print(' ', end='')
            print('*', end='')
        print()

def func(k):
    global n
    if k==1:
        check(k)
        return
    else:
        func(k-1)
        check(k)
        

func(n)
        
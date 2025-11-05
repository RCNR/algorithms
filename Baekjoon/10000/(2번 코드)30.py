# 10610
n = input()

if not '0' in n or sum(map(int, n)) % 3 != 0:
    print(-1)
else:
    print(''.join(sorted(n, reverse=True)))

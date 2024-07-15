# 16499

ary = dict()
num = int(input())

for _ in range(num):
    str = input()
    new_str = ''.join(sorted(str))
    ary[new_str] = 1

print(len(ary))

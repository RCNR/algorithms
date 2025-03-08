# Gnome Sequencing 4589
import sys
input = sys.stdin.readline

n = int(input())

print("Gnomes:")
for _ in range(n):
    ary = list(map(int, input().split()))
    if ary[0] >= ary[1]: res = 0
    else: res = 1
    flag = True
    for i in range(2, len(ary)):
        if ary[i-1] >= ary[i]:
            check = 0
        else:
            check = 1
        if res != check:
            print("Unordered")
            flag = False
            break
    if flag:
        print("Ordered")
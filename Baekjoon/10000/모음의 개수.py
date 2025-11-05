ary = input()
cnt = sum(1 for k in ary if k in 'aeiou')
print(cnt)